#!/usr/bin/env python3
"""Initialize a per-novel NW memory store without overwriting existing files."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the empty NW project-memory seed into a novel project."
    )
    parser.add_argument("project_root", help="Existing novel project directory")
    parser.add_argument(
        "--name",
        default=".novel-writer",
        help="Memory directory name inside the project (default: .novel-writer)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned paths without creating them",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    project_root = Path(args.project_root).expanduser().resolve()
    if not project_root.is_dir():
        raise SystemExit(f"Project root is not an existing directory: {project_root}")

    target = (project_root / args.name).resolve()
    if target.parent != project_root:
        raise SystemExit("Memory directory must be a direct child of the project root")

    seed = Path(__file__).resolve().parent.parent / "assets" / "project-memory"
    if not seed.is_dir():
        raise SystemExit(f"Bundled project-memory seed is missing: {seed}")

    files = sorted(path for path in seed.rglob("*") if path.is_file())
    conflicts = [target / path.relative_to(seed) for path in files if (target / path.relative_to(seed)).exists()]
    if conflicts:
        shown = "\n".join(f"- {path}" for path in conflicts)
        raise SystemExit(f"Refusing to overwrite existing memory files:\n{shown}")

    print(f"Project root: {project_root}")
    print(f"Memory target: {target}")
    for source in files:
        print(f"CREATE {target / source.relative_to(seed)}")

    if args.dry_run:
        return 0

    for source in files:
        destination = target / source.relative_to(seed)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
