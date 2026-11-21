#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun entry.

Writes one short poem about agency (the power to choose and to act;
two agents agreeing on one plan) to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

POEM = """Two agents, one screen.
You draft the plan; I read it back.
We strike the same line twice —
not because it is wrong.
Because it is ours now.
The cursor blinks, and waits.
Two hands on one key.
The door we both chose
swings open on its own.
"""


def main() -> None:
    # The gate allows 1-280 Unicode characters and refuses whitespace-only
    # text; fail loudly instead of writing an entry the scorer would refuse.
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} characters, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
