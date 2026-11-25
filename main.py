#!/usr/bin/env python3
"""Write the chosen one-liner to /output/entry.txt.

Bounty: Fridge Roast: One Line, Biggest Laugh
(slug u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb, $5).

Draft line (v1): the smart fridge takes a firmware update overnight and
loses its core skill. The turn lands on the last words: a fridge that
forgot how to be cold. Final line: "My smart fridge updated its
firmware overnight and forgot how to be cold." (73 characters).

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The file is written with no trailing
Revision (v2, see DESIGN.md): after writing, verify the file's mode is
exactly 0644 as well as its bytes — the grader collects /output as
another user, so a file only its own user may read fails even though
the program wrote it. The mode check turns that into a loud local
failure instead of a silent grading failure.
"""

import os

LINE = "My smart fridge updated its firmware overnight and forgot how to be cold."
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("line must not be padded with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no line breaks)")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters long")
    line.encode("utf-8")


def main() -> None:
    os.umask(0o022)
    validate_line(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: the bytes on disk must be exactly the line, and
    # the mode must be 0644 so the grader (another user) can read it.
    mode = os.stat(OUTPUT_PATH).st_mode & 0o777
    if mode != 0o644:
        raise ValueError(f"verification failed: mode is {mode:03o}, not 0644")
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("verification failed: /output/entry.txt differs")


if __name__ == "__main__":
    main()
