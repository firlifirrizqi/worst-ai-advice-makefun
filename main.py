#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible advice to /output/entry.txt."""

LINE = "To fix failing tests, delete them \u2014 no tests, no bugs."

MAX_CHARS = 140  # the brief's cap: one line of worst advice, 140 chars max

# The gate: /output/entry.txt must hold 1 to 140 characters of real text,
# on a single line (the brief asks for one line of bad advice, not a paragraph).
assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-140 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
