#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology
to /output/entry.txt, deterministically.

Craft notes:
- The patch-note form works because it treats a human flaw as a
  software bug: the dry, clinical "fixed a bug where ..." framing
  collides with a deeply relatable experience, so the joke lands
  on the incongruity between the format and the subject.
- The 2009-vs-now contrast lands because the brain's memory is
  shown as both overpowered (it kept every embarrassment since
  2009) and broken (it lost the reason you entered this room
  seconds ago) — the asymmetry makes the bug feel specific and
  true, not generic.
- The version string "v3.2.0" sells the changelog illusion in a
  single token.

Gate: the entry must be 1-160 chars of non-whitespace UTF-8 text
in /output/entry.txt; see the asserts in main().
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
