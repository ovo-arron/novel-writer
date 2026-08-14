#!/usr/bin/env python3
"""Create a new, allowlisted NW skill clone without touching local projects."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ALLOWED_ROOT_FILES = {"SKILL.md", "LICENSE"}
ALLOWED_ROOT_DIRS = {"agents", "assets", "evals", "references", "scripts"}
EXCLUDED_PARTS = {"__pycache__", ".git", ".novel-writer"}
EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".bak",
    ".tmp",
    ".docx",
    ".epub",
}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy universal NW files and blank templates into a new skill directory. "
            "The destination must not exist."
        )
    )
    parser.add_argument("destination", type=Path)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="NW skill source (default: the installed skill containing this script)",
    )
    parser.add_argument(
        "--deny-token",
        action="append",
        default=[],
        help="Reject the clone if this private project marker appears; repeat as needed",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List allowlisted files without creating the destination",
    )
    return parser.parse_args()


def is_allowlisted(relative: Path) -> bool:
    if not relative.parts or any(part in EXCLUDED_PARTS for part in relative.parts):
        return False
    if len(relative.parts) == 1:
        return relative.name in ALLOWED_ROOT_FILES
    if relative.parts[0] not in ALLOWED_ROOT_DIRS:
        return False
    if relative.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if relative.parts[0] == "scripts" and relative.suffix.lower() != ".py":
        return False
    return True


def scan_text(root: Path, deny_tokens: list[str]) -> list[str]:
    errors: list[str] = []
    generic_markers = (
        "C:" + "\\Users\\",
        "/" + "Users/",
        "/" + "home/",
        "codex-" + "remote-attachments",
    )
    folded_tokens = [token.casefold() for token in deny_tokens if token.strip()]
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        relative = path.relative_to(root)
        folded = text.casefold()
        for marker in generic_markers:
            if marker.casefold() in folded:
                errors.append(f"local path marker in {relative}: {marker}")
        for token in folded_tokens:
            if token in folded:
                errors.append(f"denied private token in {relative}: {token}")
    return errors


def main() -> int:
    args = parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")

    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Source is not an NW skill directory: {source}")
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing destination: {destination}")
    if destination == source or source in destination.parents or destination in source.parents:
        raise SystemExit("Source and destination must be separate, non-nested directories")

    files = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and is_allowlisted(path.relative_to(source))
    )
    if not files:
        raise SystemExit("No allowlisted files found")

    print(f"Source: {source}")
    print(f"Destination: {destination}")
    for source_file in files:
        print(f"COPY {source_file.relative_to(source)}")
    if args.dry_run:
        return 0

    for source_file in files:
        target = destination / source_file.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target)

    errors = scan_text(destination, args.deny_token)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(
            "Clone was created but failed the privacy scan; do not publish it.",
            file=sys.stderr,
        )
        return 1

    print(f"PASS: created public-skill clone with {len(files)} allowlisted files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
