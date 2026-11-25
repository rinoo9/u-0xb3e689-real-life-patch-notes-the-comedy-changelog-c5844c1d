#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology
to /output/entry.txt, deterministically.

Craft notes (revision round 3, 25 Nov 2026):
- The patch-note form works because it treats a human flaw as a
  software bug: the dry, clinical "fixed a bug where ..." framing
  collides with a deeply relatable experience, so the joke lands
  on the incongruity between the format and the subject.
- The previous line blamed the user for creaky knees; this one
  picks a different everyday bug — the snooze button — and the
  punchline is a billing joke: the patch "fixes" the guilt by
  charging for it separately, which is exactly how software
  monetises a problem instead of solving it. Nine minutes of
  sleep versus three hours of guilt is the asymmetric trade that
  makes the bug feel specific and true, not generic.
- The version string "v2.0.1" sells the changelog illusion in a
  single token.

Gate: the entry must be 1-160 chars of non-whitespace UTF-8 text
in /output/entry.txt; see the asserts in main().
"""

import os

ENTRY = (
    "v2.0.1: fixed a bug where the snooze button granted nine extra "
    "minutes of sleep and three hours of guilt; guilt is now billed separately."
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
