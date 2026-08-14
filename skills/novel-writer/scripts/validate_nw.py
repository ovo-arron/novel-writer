#!/usr/bin/env python3
"""Validate NW's lightweight structure and evaluation inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT_LINK = re.compile(r"`((?:references|scripts|assets)/[^`]+)`")
REQUIRED_CASE_KEYS = {"id", "task", "must_show", "must_avoid"}
REQUIRED_SKILL_FILES = {
    "LICENSE",
    "agents/openai.yaml",
    "references/adaptation-router.md",
    "references/narrative-engines.md",
    "references/sources-and-lineage.md",
    "references/three-core-orchestration.md",
    "assets/project-memory/adaptation-profile.md",
    "assets/project-memory/unit-ledger.md",
    "scripts/build_public_clone.py",
}
UNIVERSAL_TRIGGER_TERMS = {
    "short stories",
    "novellas",
    "literary and contemporary fiction",
    "romance",
    "historical fiction",
    "mystery",
    "horror",
    "science fiction",
    "fantasy",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


PUBLIC_ROOT_FILES = {"SKILL.md", "LICENSE"}
PUBLIC_ROOT_DIRS = {"agents", "assets", "evals", "references", "scripts"}
PUBLIC_BLOCKED_PARTS = {"__pycache__", ".git", ".novel-writer"}
PUBLIC_BLOCKED_SUFFIXES = {
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


def validate(
    skill_root: Path,
    deny_tokens: tuple[str, ...] = (),
    public_release: bool = False,
) -> list[str]:
    errors: list[str] = []
    skill_file = skill_root / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    skill_text = skill_file.read_text(encoding="utf-8")
    skill_lines = skill_text.splitlines()
    if len(skill_lines) > 500:
        fail(errors, f"SKILL.md has {len(skill_lines)} lines; keep it under 500")

    for relative in sorted(REQUIRED_SKILL_FILES):
        if not (skill_root / relative).is_file():
            fail(errors, f"missing required portable file: {relative}")

    frontmatter = re.match(r"\A---\n(.*?)\n---", skill_text, flags=re.DOTALL)
    if not frontmatter:
        fail(errors, "SKILL.md lacks valid opening frontmatter")
    elif len(frontmatter.group(1)) > 1024:
        fail(errors, "SKILL.md frontmatter exceeds 1024 characters")

    lowered_skill = skill_text.lower()
    for term in sorted(UNIVERSAL_TRIGGER_TERMS):
        if term not in lowered_skill:
            fail(errors, f"universal trigger coverage missing: {term}")

    for markdown in [skill_file, *sorted((skill_root / "references").glob("*.md"))]:
        text = markdown.read_text(encoding="utf-8")
        for relative in ROOT_LINK.findall(text):
            target = skill_root / relative.split()[0]
            if not target.exists():
                fail(errors, f"broken root link in {markdown.name}: {relative}")

    references = sorted((skill_root / "references").glob("*.md"))
    for reference in references:
        lines = reference.read_text(encoding="utf-8").splitlines()
        if len(lines) > 100 and not any(
            line.strip() == "## Contents" for line in lines[:40]
        ):
            fail(errors, f"long reference lacks early Contents section: {reference.name}")

    cases_file = skill_root / "evals" / "cases.json"
    try:
        cases = json.loads(cases_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot read evals/cases.json: {exc}")
        return errors

    if not isinstance(cases, list):
        fail(errors, "evals/cases.json must contain a list")
        return errors

    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(errors, f"case {index} is not an object")
            continue
        missing = REQUIRED_CASE_KEYS - case.keys()
        if missing:
            fail(errors, f"case {index} missing keys: {sorted(missing)}")
            continue
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id.strip():
            fail(errors, f"case {index} has invalid id")
        elif case_id in seen:
            fail(errors, f"duplicate case id: {case_id}")
        else:
            seen.add(case_id)
        if not isinstance(case["task"], str) or not case["task"].strip():
            fail(errors, f"case {case_id!r} has invalid task")
        for key in ("must_show", "must_avoid"):
            values = case[key]
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                fail(errors, f"case {case_id!r} has invalid {key}")

    triggers_file = skill_root / "evals" / "trigger-queries.json"
    try:
        triggers = json.loads(triggers_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot read evals/trigger-queries.json: {exc}")
        return errors
    if not isinstance(triggers, list) or not triggers:
        fail(errors, "evals/trigger-queries.json must contain a non-empty list")
    else:
        for index, trigger in enumerate(triggers):
            if not isinstance(trigger, dict):
                fail(errors, f"trigger {index} is not an object")
                continue
            if not isinstance(trigger.get("query"), str) or not trigger["query"].strip():
                fail(errors, f"trigger {index} has invalid query")
            if not isinstance(trigger.get("should_trigger"), bool):
                fail(errors, f"trigger {index} has invalid should_trigger")

    public_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in skill_root.rglob("*")
        if path.is_file()
        and path.resolve() != Path(__file__).resolve()
        and path.suffix.lower() in {".md", ".json", ".yaml", ".py"}
    )
    private_patterns = (
        "C:" + "\\Users\\",
        "codex-" + "remote-attachments",
    )
    folded_public_text = public_text.casefold()
    for private_pattern in (*private_patterns, *deny_tokens):
        if not private_pattern:
            continue
        if private_pattern.casefold() in folded_public_text:
            fail(errors, f"possible local/private release residue: {private_pattern}")

    if public_release:
        for path in skill_root.rglob("*"):
            relative = path.relative_to(skill_root)
            if any(part in PUBLIC_BLOCKED_PARTS for part in relative.parts):
                fail(errors, f"blocked public-release path: {relative}")
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() in PUBLIC_BLOCKED_SUFFIXES:
                fail(errors, f"blocked public-release file type: {relative}")
            if len(relative.parts) == 1 and relative.name not in PUBLIC_ROOT_FILES:
                fail(errors, f"unexpected public skill root file: {relative}")
            if len(relative.parts) > 1 and relative.parts[0] not in PUBLIC_ROOT_DIRS:
                fail(errors, f"unexpected public skill root directory: {relative.parts[0]}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "skill_root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--public-release",
        action="store_true",
        help="Reject caches, project memory instances, derived indexes, and extra root files",
    )
    parser.add_argument(
        "--deny-token",
        action="append",
        default=[],
        help="Reject a known private project marker; repeat as needed",
    )
    args = parser.parse_args()
    root = args.skill_root.resolve()
    errors = validate(root, tuple(args.deny_token), args.public_release)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    cases = json.loads((root / "evals" / "cases.json").read_text(encoding="utf-8"))
    references = list((root / "references").glob("*.md"))
    triggers = json.loads(
        (root / "evals" / "trigger-queries.json").read_text(encoding="utf-8")
    )
    skill_lines = len((root / "SKILL.md").read_text(encoding="utf-8").splitlines())
    print(
        f"PASS: NW structure valid; {len(cases)} eval cases, "
        f"{len(triggers)} trigger queries, {len(references)} references, "
        f"SKILL.md {skill_lines} lines"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
