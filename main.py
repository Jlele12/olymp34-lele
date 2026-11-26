#!/usr/bin/env python3
"""Entry for Rejected Olympic Sports (u-motasimfuad-rejected-olympic-sports-9d83e7da).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "Competitive alarm clock snoozing: longest ignore wins, and you still claim you meant to get up."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
