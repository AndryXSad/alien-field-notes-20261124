#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun bounty entry.

Writes a single one-line review of planet Earth, left by an alien tourist
(at most 200 characters), to /output/entry.txt, where the house judge reads it.
Standard library only.

The line (142 characters): an alien tourist's outsider view of an everyday
Earth truth — humans built a machine to wash the dishes, then stand beside
it arguing about whose turn it is to load it. One clean joke, the punch at
the end, closed like a real review: five stars, would visit again.
"""

import os
from pathlib import Path

LINE = (
    "They invented a machine that washes the dishes, then stand beside it "
    "arguing about whose turn it is to load it. Five stars, would visit again."
)


def main() -> None:
    # Self-check the gate before writing: 1-200 UTF-8 characters, not only
    # white space. The line is 142 characters.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
