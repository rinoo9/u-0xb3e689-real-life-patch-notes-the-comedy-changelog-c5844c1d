#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology
to /output/entry.txt, deterministically.
"""

import os

ENTRY = (
    "v3.2.0: fixed a bug where the brain saved every embarrassing "
    "moment since 2009 but forgot why you walked into this room."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 160
    # characters, not only white space.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
