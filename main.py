#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt.

The line: legacy code is a love letter from a developer who has already
left, and the reader is told to read it twice before rewriting its
ending — a quiet twist on the rewrite instinct every tired senior knows.
"""

import os
import sys

FORTUNE = "Legacy code is a love letter from a developer who left; read it twice before you rewrite the ending."


def validate(text: str) -> bool:
    """The gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    return bool(text.strip()) and 1 <= len(text) <= 120


def main() -> int:
    if not validate(FORTUNE):
        print("fortune fails the gate", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
