#!/usr/bin/env python3
"""Funniest Autocorrect Fail - entry program.

Writes a single autocorrect-fail line to /output/entry.txt.
"""

import os

LINE = "Hi, it's apartment 4B \u2014 the toilet is pregnant again. Can you send a plumber before it gives birth?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
