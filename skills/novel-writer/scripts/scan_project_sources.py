#!/usr/bin/env python3
"""Read-only inventory of likely novel-project sources for NW Core III."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md", ".markdown", ".txt", ".docx", ".odt", ".rtf", ".pdf", ".csv", ".json", ".yaml", ".yml"
}
EXCLUDED_DIRS = {
    ".git", ".novel-writer", ".idea", ".vscode", "node_modules", "__pycache__",
    "backup", "backups", "备份", "export", "exports", "导出", "dist", "build",
    ".cache", "cache", "缓存", ".codex-review"
}
ROLE_HINTS = {
    "manuscript": ("chapter", "chapters", "manuscript", "正文", "章节", "稿"),
    "outline": ("outline", "plot", "大纲", "剧情", "卷纲", "章纲"),
    "bible": ("bible", "setting", "world", "设定", "世界观", "资料"),
    "character": ("character", "cast", "人物", "角色", "人设"),
    "correction": ("correction", "feedback", "revision", "修改", "反馈", "校对"),
    "reference": ("reference", "research", "参考", "资料来源"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List likely manuscript, outline, bible, and correction sources without editing them."
    )
    parser.add_argument("project_root", help="Existing novel project directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--max-files", type=int, default=2000, help="Safety cap (default: 2000)")
    return parser.parse_args()


def infer_roles(relative_path: Path) -> list[str]:
    text = str(relative_path).casefold()
    roles = [role for role, hints in ROLE_HINTS.items() if any(hint.casefold() in text for hint in hints)]
    return roles or ["unclassified"]


def excluded(relative_path: Path) -> bool:
    for part in relative_path.parts[:-1]:
        folded = part.casefold()
        if folded in EXCLUDED_DIRS or folded.startswith(".tmp"):
            return True
    return False


def main() -> int:
    args = parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    root = Path(args.project_root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Project root is not an existing directory: {root}")
    if args.max_files < 1:
        raise SystemExit("--max-files must be positive")

    records: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        relative_path = path.relative_to(root)
        if excluded(relative_path):
            continue
        if not path.is_file() or path.suffix.casefold() not in TEXT_EXTENSIONS:
            continue
        try:
            path.resolve().relative_to(root)
        except ValueError:
            continue
        stat = path.stat()
        records.append({
            "path": str(relative_path),
            "extension": path.suffix.casefold(),
            "size_bytes": stat.st_size,
            "modified_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            "role_candidates": infer_roles(relative_path),
        })
        if len(records) >= args.max_files:
            break

    payload = {
        "project_root": str(root),
        "read_only": True,
        "candidate_count": len(records),
        "reached_safety_cap": len(records) >= args.max_files,
        "candidates": records,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Project root: {root}")
        print(f"Candidate sources: {len(records)}")
        for record in records:
            roles = ",".join(record["role_candidates"])
            print(f"{roles}\t{record['size_bytes']}\t{record['path']}")
        if payload["reached_safety_cap"]:
            print("WARNING: safety cap reached; results may be incomplete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
