#!/usr/bin/env python3
"""Calculate a transparent whole-book chapter and volume scale."""

from __future__ import annotations

import argparse
import json
import math
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert target characters and chapter size into chapter/volume ranges without inventing plot."
    )
    parser.add_argument("--total-characters", "--total-words", dest="total_characters", type=int, required=True)
    parser.add_argument("--characters-per-chapter", "--words-per-chapter", dest="characters_per_chapter", type=int, required=True)
    parser.add_argument("--volumes", type=int)
    parser.add_argument("--target-chapters-per-volume", type=int, default=40)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def calculate(total_characters: int, characters_per_chapter: int, volumes: int | None, target: int) -> dict:
    if min(total_characters, characters_per_chapter, target) <= 0 or (volumes is not None and volumes <= 0):
        raise SystemExit("All numeric inputs must be positive")
    chapters = math.ceil(total_characters / characters_per_chapter)
    volume_count = volumes or max(1, round(chapters / target))
    base, extra = divmod(chapters, volume_count)
    ranges = []
    start = 1
    for volume in range(1, volume_count + 1):
        count = base + (1 if volume <= extra else 0)
        end = start + count - 1
        ranges.append({"volume": volume, "start_chapter": start, "end_chapter": end, "chapters": count})
        start = end + 1
    return {
        "target_characters": total_characters,
        "characters_per_chapter": characters_per_chapter,
        "estimated_chapters": chapters,
        "estimated_characters_at_full_chapters": chapters * characters_per_chapter,
        "volumes": volume_count,
        "average_chapters_per_volume": round(chapters / volume_count, 2),
        "ranges": ranges,
        "note": "This is a capacity map, not a plot allocation. Adjust boundaries to causal settlements.",
    }


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    args = parse_args()
    result = calculate(args.total_characters, args.characters_per_chapter, args.volumes, args.target_chapters_per_volume)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Target: {result['target_characters']} characters")
        print(f"Estimated chapters: {result['estimated_chapters']}")
        print(f"Volumes: {result['volumes']}")
        for row in result["ranges"]:
            print(f"Volume {row['volume']}: chapters {row['start_chapter']}-{row['end_chapter']} ({row['chapters']})")
        print(result["note"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
