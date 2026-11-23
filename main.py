#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to /output/entry.txt: A for coffee.
Deterministic: the same bytes on every run. The letter is a
constant in this file; nothing is read from the working directory,
so the program does not depend on process.cwd().
"""

import os

LINE = "A"
# Exactly one letter, A for coffee or B for tea, and nothing else.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
