#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology
to /output/entry.txt, deterministically.

Craft notes (revision round 4, 26 Nov 2026):
- The patch-note form works because it treats a human flaw as a
  software bug: the dry, clinical "fixed a bug where ..." framing
  collides with a deeply relatable experience, so the joke lands
  on the incongruity between the format and the subject.
- The previous line billed guilt separately; this one picks a
  different everyday bug — the Wi-Fi that only ever drops at the
  worst possible moment — and the punchline is a fake fix: the
  patch does not stop the drops, it just reschedules them to the
  boring part of the call, which is exactly how software ships a
  workaround and calls it a fix. Everyone has lived the important
  part cutting out mid-sentence, so the bug feels specific and
  true, not generic.
- The version string "v4.1.0" sells the changelog illusion in a
  single token.

Gate: the entry must be 1-160 chars of non-whitespace UTF-8 text
in /output/entry.txt; see the asserts in main().
"""

import os

ENTRY = (
    "v4.1.0: fixed a bug where the Wi-Fi dropped only during the "
    "important part of the call; it now drops during the boring part instead."
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
