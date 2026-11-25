#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun program/v1 entry.

Writes one fortune cookie line to /output/entry.txt.
The line is fixed, so every run produces byte-identical output.
"""

import os

FORTUNE = "A stranger will ask you to write a poem about their cat. You will. You always do."


def main() -> None:
    # Gate self-check: the competition's scorer requires UTF-8 text of
    # 1-200 characters, not only white space, on a single line.
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune is {len(text)} chars, gate needs 1-200"
    assert "\n" not in text and "\r" not in text, "fortune must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
