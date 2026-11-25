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


def _validate(line: str) -> str:
    # Self-check the gate before writing: 1-200 UTF-8 characters, not only
    # white space. The line is 142 characters.
    if not 1 <= len(line) <= 200 or not line.strip():
        raise SystemExit("line fails the 1-200 character gate")
    return line


def _output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def _write(line: str) -> None:
    entry_path = _output_path()
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(line, encoding="utf-8")


def main() -> None:
    line = _validate(LINE)
    _write(line)
    print(line)


if __name__ == "__main__":
    main()
