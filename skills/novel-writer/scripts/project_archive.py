#!/usr/bin/env python3
"""Build and query a local, incremental NW archive for very long novels."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".markdown", ".txt"}
EXCLUDED_DIRS = {
    ".git", ".idea", ".vscode", "node_modules", "__pycache__", ".cache",
    "cache", "缓存", "backup", "backups", "备份", "export", "exports", "导出",
    "dist", "build", ".codex-review", "index",
}
HEADING_RE = re.compile(
    r"^(?:#{1,6}\s+.+|第[〇零一二三四五六七八九十百千万两0-9]+[章节卷回部篇](?:\s+.*)?)\s*$"
)


def configure_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Incremental local archive for multi-million-character NW projects."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="Build or incrementally refresh the local index")
    build.add_argument("project_root")
    build.add_argument("--chunk-chars", type=int, default=4500)
    build.add_argument("--overlap-chars", type=int, default=300)
    build.add_argument("--json", action="store_true")

    search = sub.add_parser("search", help="Search indexed source text")
    search.add_argument("project_root")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=8)
    search.add_argument(
        "--scope", choices=("all", "source", "memory"), default="all",
        help="Search all indexed text, authoritative/project sources only, or NW memory only",
    )
    search.add_argument("--json", action="store_true")

    status = sub.add_parser("status", help="Show archive size and freshness")
    status.add_argument("project_root")
    status.add_argument("--json", action="store_true")

    test = sub.add_parser("self-test", help="Run a synthetic scale and retrieval test")
    test.add_argument("--chars", type=int, default=1_200_000)
    return parser.parse_args()


def resolve_root(raw: str) -> Path:
    root = Path(raw).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Project root is not an existing directory: {root}")
    return root


def archive_path(root: Path) -> Path:
    target = (root / ".novel-writer" / "index" / "project-index.sqlite3").resolve()
    target.relative_to(root)
    return target


def excluded(relative: Path) -> bool:
    for part in relative.parts[:-1]:
        folded = part.casefold()
        if folded == ".novel-writer":
            continue
        if folded in EXCLUDED_DIRS or folded.startswith(".tmp"):
            return True
    return False


def iter_sources(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if excluded(relative) or path.suffix.casefold() not in TEXT_EXTENSIONS:
            continue
        try:
            path.resolve().relative_to(root)
        except ValueError:
            continue
        yield path, relative


def classify_role(relative: Path) -> str:
    if relative.parts and relative.parts[0].casefold() == ".novel-writer":
        return "memory"
    text = str(relative).casefold()
    hints = (
        ("manuscript", ("正文", "章节", "chapter", "manuscript")),
        ("outline", ("大纲", "卷纲", "章纲", "outline", "plot")),
        ("bible", ("设定", "世界观", "人物", "角色", "bible", "setting", "character")),
        ("feedback", ("反馈", "修改", "校对", "feedback", "correction", "revision")),
    )
    for role, tokens in hints:
        if any(token in text for token in tokens):
            return role
    return "source"


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeError(f"Unsupported text encoding: {path}")


def split_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    heading = ""
    buffer: list[str] = []
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if HEADING_RE.match(stripped) and buffer:
            sections.append((heading, "".join(buffer)))
            heading, buffer = stripped, [line]
        else:
            if HEADING_RE.match(stripped):
                heading = stripped
            buffer.append(line)
    if buffer:
        sections.append((heading, "".join(buffer)))
    return sections


def chunk_section(heading: str, text: str, max_chars: int, overlap: int):
    if len(text) <= max_chars:
        yield heading, 0, len(text), text
        return
    start = 0
    while start < len(text):
        hard_end = min(len(text), start + max_chars)
        end = hard_end
        if hard_end < len(text):
            floor = start + max_chars // 2
            candidates = [text.rfind("\n\n", floor, hard_end), text.rfind("\n", floor, hard_end)]
            end = max(candidates)
            if end <= start:
                end = hard_end
        piece = text[start:end].strip()
        if piece:
            yield heading, start, end, piece
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)


def make_chunks(text: str, max_chars: int, overlap: int):
    ordinal = 0
    absolute = 0
    for heading, section in split_sections(text):
        section_start = text.find(section, absolute)
        if section_start < 0:
            section_start = absolute
        for local_heading, start, end, piece in chunk_section(heading, section, max_chars, overlap):
            ordinal += 1
            yield ordinal, local_heading, section_start + start, section_start + end, piece
        absolute = section_start + len(section)


def connect(db_path: Path, writable: bool) -> sqlite3.Connection:
    if writable:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(db_path)
    else:
        if not db_path.is_file():
            raise SystemExit(f"Archive does not exist; run build first: {db_path}")
        connection = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def init_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS files (
          id INTEGER PRIMARY KEY,
          path TEXT NOT NULL UNIQUE,
          role TEXT NOT NULL,
          size_bytes INTEGER NOT NULL,
          char_count INTEGER NOT NULL DEFAULT 0,
          mtime_ns INTEGER NOT NULL,
          sha256 TEXT NOT NULL,
          indexed_at TEXT NOT NULL,
          chunk_count INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS chunks (
          id INTEGER PRIMARY KEY,
          file_id INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
          ordinal INTEGER NOT NULL,
          heading TEXT NOT NULL,
          start_char INTEGER NOT NULL,
          end_char INTEGER NOT NULL,
          text TEXT NOT NULL,
          UNIQUE(file_id, ordinal)
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(text, tokenize='trigram');
        CREATE INDEX IF NOT EXISTS chunks_file_id ON chunks(file_id);
        """
    )
    columns = {row[1] for row in connection.execute("PRAGMA table_info(files)")}
    if "char_count" not in columns:
        connection.execute(
            "ALTER TABLE files ADD COLUMN char_count INTEGER NOT NULL DEFAULT 0"
        )


def delete_file_chunks(connection: sqlite3.Connection, file_id: int) -> None:
    rowids = [row[0] for row in connection.execute("SELECT id FROM chunks WHERE file_id=?", (file_id,))]
    if rowids:
        connection.executemany("DELETE FROM chunks_fts WHERE rowid=?", [(rowid,) for rowid in rowids])
    connection.execute("DELETE FROM chunks WHERE file_id=?", (file_id,))


def build_archive(root: Path, chunk_chars: int, overlap: int) -> dict[str, object]:
    if chunk_chars < 1000:
        raise SystemExit("--chunk-chars must be at least 1000")
    if overlap < 0 or overlap >= chunk_chars // 2:
        raise SystemExit("--overlap-chars must be non-negative and less than half the chunk size")
    db_path = archive_path(root)
    connection = connect(db_path, writable=True)
    init_schema(connection)
    existing = {row["path"]: row for row in connection.execute("SELECT * FROM files")}
    seen: set[str] = set()
    changed = unchanged = skipped = 0

    for path, relative in iter_sources(root):
        rel_text = relative.as_posix()
        seen.add(rel_text)
        stat = path.stat()
        prior = existing.get(rel_text)
        if (
            prior
            and prior["char_count"] > 0
            and prior["size_bytes"] == stat.st_size
            and prior["mtime_ns"] == stat.st_mtime_ns
        ):
            unchanged += 1
            continue
        digest = file_hash(path)
        try:
            text = read_text(path)
        except (OSError, UnicodeError):
            skipped += 1
            continue
        if prior and prior["sha256"] == digest:
            connection.execute(
                "UPDATE files SET size_bytes=?, char_count=?, mtime_ns=?, indexed_at=? WHERE id=?",
                (stat.st_size, len(text), stat.st_mtime_ns, now_iso(), prior["id"]),
            )
            unchanged += 1
            continue
        role = classify_role(relative)
        if prior:
            file_id = int(prior["id"])
            delete_file_chunks(connection, file_id)
            connection.execute(
                "UPDATE files SET role=?, size_bytes=?, char_count=?, mtime_ns=?, sha256=?, indexed_at=?, chunk_count=0 WHERE id=?",
                (role, stat.st_size, len(text), stat.st_mtime_ns, digest, now_iso(), file_id),
            )
        else:
            cursor = connection.execute(
                "INSERT INTO files(path,role,size_bytes,char_count,mtime_ns,sha256,indexed_at) VALUES(?,?,?,?,?,?,?)",
                (rel_text, role, stat.st_size, len(text), stat.st_mtime_ns, digest, now_iso()),
            )
            file_id = int(cursor.lastrowid)
        count = 0
        for ordinal, heading, start, end, piece in make_chunks(text, chunk_chars, overlap):
            cursor = connection.execute(
                "INSERT INTO chunks(file_id,ordinal,heading,start_char,end_char,text) VALUES(?,?,?,?,?,?)",
                (file_id, ordinal, heading, start, end, piece),
            )
            connection.execute("INSERT INTO chunks_fts(rowid,text) VALUES(?,?)", (cursor.lastrowid, piece))
            count += 1
        connection.execute("UPDATE files SET chunk_count=? WHERE id=?", (count, file_id))
        changed += 1

    deleted = 0
    for rel_text, row in existing.items():
        if rel_text not in seen:
            delete_file_chunks(connection, int(row["id"]))
            connection.execute("DELETE FROM files WHERE id=?", (row["id"],))
            deleted += 1
    connection.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('last_build',?)", (now_iso(),))
    connection.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('chunk_chars',?)", (str(chunk_chars),))
    connection.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('overlap_chars',?)", (str(overlap),))
    connection.commit()
    totals = connection.execute(
        "SELECT COUNT(*) files, "
        "COALESCE(SUM(CASE WHEN role!='memory' THEN size_bytes ELSE 0 END),0) source_bytes, "
        "COALESCE(SUM(CASE WHEN role='memory' THEN size_bytes ELSE 0 END),0) memory_bytes, "
        "COALESCE(SUM(CASE WHEN role!='memory' THEN char_count ELSE 0 END),0) source_characters, "
        "COALESCE(SUM(CASE WHEN role='memory' THEN char_count ELSE 0 END),0) memory_characters, "
        "COALESCE(SUM(chunk_count),0) chunks FROM files"
    ).fetchone()
    connection.close()
    return {
        "project_root": str(root), "archive": str(db_path), "changed": changed,
        "unchanged": unchanged, "deleted": deleted, "skipped": skipped,
        "files": totals["files"], "source_bytes": totals["source_bytes"],
        "source_characters": totals["source_characters"],
        "memory_bytes": totals["memory_bytes"],
        "memory_characters": totals["memory_characters"], "chunks": totals["chunks"],
    }


def scope_sql(scope: str) -> str:
    if scope == "source":
        return " AND f.role!='memory'"
    if scope == "memory":
        return " AND f.role='memory'"
    return ""


def search_archive(root: Path, query: str, limit: int, scope: str = "all") -> dict[str, object]:
    query = query.strip()
    if not query:
        raise SystemExit("Search query cannot be empty")
    connection = connect(archive_path(root), writable=False)
    role_filter = scope_sql(scope)
    params: tuple[object, ...]
    if len(query) >= 3:
        phrase = '"' + query.replace('"', '""') + '"'
        sql = f"""
          SELECT c.id,c.heading,c.start_char,c.end_char,c.text,f.path,f.role,
                 bm25(chunks_fts) score
          FROM chunks_fts JOIN chunks c ON c.id=chunks_fts.rowid
          JOIN files f ON f.id=c.file_id WHERE chunks_fts MATCH ? {role_filter}
          ORDER BY score LIMIT ?
        """
        rows = list(connection.execute(sql, (phrase, limit)))
    else:
        rows = []
    if not rows:
        terms = [term for term in re.split(r"\s+", query) if term]
        where = " AND ".join("c.text LIKE ?" for _ in terms)
        sql = f"""
          SELECT c.id,c.heading,c.start_char,c.end_char,c.text,f.path,f.role,0.0 score
          FROM chunks c JOIN files f ON f.id=c.file_id WHERE {where} {role_filter}
          ORDER BY f.path,c.ordinal LIMIT ?
        """
        params = tuple(f"%{term}%" for term in terms) + (limit,)
        rows = list(connection.execute(sql, params))
    results = []
    for row in rows:
        text = row["text"]
        at = text.find(query)
        if at < 0:
            at = 0
        start = max(0, at - 160)
        end = min(len(text), at + len(query) + 240)
        results.append({
            "path": row["path"], "role": row["role"], "heading": row["heading"],
            "start_char": row["start_char"], "end_char": row["end_char"],
            "excerpt": text[start:end].strip(), "score": row["score"],
        })
    connection.close()
    return {"query": query, "scope": scope, "count": len(results), "results": results}


def archive_status(root: Path) -> dict[str, object]:
    db_path = archive_path(root)
    connection = connect(db_path, writable=False)
    totals = connection.execute(
        "SELECT COUNT(*) files,"
        "COALESCE(SUM(CASE WHEN role!='memory' THEN size_bytes ELSE 0 END),0) source_bytes,"
        "COALESCE(SUM(CASE WHEN role='memory' THEN size_bytes ELSE 0 END),0) memory_bytes,"
        "COALESCE(SUM(CASE WHEN role!='memory' THEN char_count ELSE 0 END),0) source_characters,"
        "COALESCE(SUM(CASE WHEN role='memory' THEN char_count ELSE 0 END),0) memory_characters,"
        "COALESCE(SUM(chunk_count),0) chunks FROM files"
    ).fetchone()
    roles = {row["role"]: row["count"] for row in connection.execute(
        "SELECT role,COUNT(*) count FROM files GROUP BY role ORDER BY role"
    )}
    meta = {row["key"]: row["value"] for row in connection.execute("SELECT key,value FROM meta")}
    connection.close()
    return {
        "project_root": str(root), "archive": str(db_path), "files": totals["files"],
        "source_bytes": totals["source_bytes"],
        "source_characters": totals["source_characters"],
        "memory_bytes": totals["memory_bytes"],
        "memory_characters": totals["memory_characters"],
        "chunks": totals["chunks"], "roles": roles,
        "last_build": meta.get("last_build"), "chunk_chars": meta.get("chunk_chars"),
        "overlap_chars": meta.get("overlap_chars"),
    }


def self_test(char_count: int) -> dict[str, object]:
    if char_count < 100_000:
        raise SystemExit("--chars must be at least 100000")
    marker = "灰塔粮仓的铜钥匙只交给夜班记录员"
    semantic_question = "她为什么始终不肯把弟弟交给军方"
    with tempfile.TemporaryDirectory(prefix="nw-archive-test-") as raw:
        root = Path(raw)
        manuscript = root / "正文"
        manuscript.mkdir()
        paragraph = "雨水沿着旧城墙往下淌。巡夜的人核对粮袋、伤员和没送到的信。"
        chapter_count = max(10, char_count // 3000)
        per_chapter = max(200, char_count // chapter_count)
        volume_count = 12
        chapters_per_volume = (chapter_count + volume_count - 1) // volume_count
        volume_paths = []
        for volume in range(1, volume_count + 1):
            volume_path = manuscript / f"第{volume:02d}卷.txt"
            volume_paths.append(volume_path)
            start_chapter = (volume - 1) * chapters_per_volume + 1
            end_chapter = min(chapter_count, volume * chapters_per_volume)
            if start_chapter > end_chapter:
                continue
            with volume_path.open("w", encoding="utf-8") as handle:
                for chapter in range(start_chapter, end_chapter + 1):
                    handle.write(f"第{chapter}章 测试章节\n")
                    body = (paragraph * (per_chapter // len(paragraph) + 1))[:per_chapter]
                    if chapter == chapter_count // 2:
                        body += marker
                    handle.write(body + "\n")
        memory_root = root / ".novel-writer"
        memory_root.mkdir()
        (memory_root / "retrieval-cues.md").write_text(
            "# Retrieval Cues\n\n"
            f"概念问题：{semantic_question}\n"
            "具体线索：灰塔粮仓、铜钥匙、夜班记录员、旧港扣押令。\n"
            "含义：军方曾绕过监护人扣押未成年人，后来归还名单缺页。\n"
            "来源：正文中含有灰塔粮仓铜钥匙记录的章节。\n",
            encoding="utf-8",
        )
        first = build_archive(root, 4500, 300)
        found = search_archive(root, marker, 5, "source")
        short_found = search_archive(root, "粮仓", 5, "source")
        semantic_found = search_archive(root, semantic_question, 5, "memory")
        bridge_found = search_archive(root, marker, 5, "source")
        second = build_archive(root, 4500, 300)
        update_marker = "增量改稿后新增的白桦渡口欠条"
        with volume_paths[-1].open("a", encoding="utf-8") as handle:
            handle.write("\n" + update_marker + "\n")
        third = build_archive(root, 4500, 300)
        updated_found = search_archive(root, update_marker, 5, "source")
        status = archive_status(root)
        passed = bool(
            found["count"]
            and short_found["count"]
            and semantic_found["count"]
            and bridge_found["count"]
            and first["source_characters"] >= char_count
            and second["changed"] == 0
            and third["changed"] == 1
            and updated_found["count"]
        )
        return {
            "passed": passed, "requested_chars": char_count,
            "indexed_characters": status["source_characters"],
            "indexed_memory_characters": status["memory_characters"],
            "indexed_bytes": status["source_bytes"], "files": status["files"],
            "chunks": status["chunks"], "marker_hits": found["count"],
            "short_query_hits": short_found["count"],
            "semantic_bridge_hits": semantic_found["count"],
            "bridge_source_hits": bridge_found["count"],
            "incremental_unchanged": second["unchanged"], "incremental_changed": second["changed"],
            "modified_files_reindexed": third["changed"],
            "updated_marker_hits": updated_found["count"],
        }


def emit(payload: dict[str, object], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    for key, value in payload.items():
        if key == "results":
            for index, result in enumerate(value, 1):
                print(f"[{index}] {result['path']} :: {result['heading']}")
                print(result["excerpt"])
        else:
            print(f"{key}: {value}")


def main() -> int:
    configure_streams()
    args = parse_args()
    if args.command == "self-test":
        result = self_test(args.chars)
        emit(result, True)
        return 0 if result["passed"] else 1
    root = resolve_root(args.project_root)
    if args.command == "build":
        emit(build_archive(root, args.chunk_chars, args.overlap_chars), args.json)
    elif args.command == "search":
        emit(search_archive(root, args.query, max(1, args.limit), args.scope), args.json)
    elif args.command == "status":
        emit(archive_status(root), args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
