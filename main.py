#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (UTF-8, 1-280 characters, not only whitespace).

The joke: a diff-grounded observation every developer who works beside
an agent recognises at once -- the agent's enormous, flawless refactor
that somehow misses the one line it was actually asked to change.
Setup ("4,000 lines, all correct") builds confidence; the punchline
("except the one line I asked it to change") reverses it in the last
clause, and the whole thing lands in a single line with no explanation.
"""

import os

JOKE = "My agent's diff was 4,000 lines, all correct \u2014 except the one line I asked it to change."


def main() -> None:
    # Self-check the house gate before writing: 1-280 Unicode code
    # points, not only whitespace, a single line. Fail loudly instead
    # of shipping an invalid entry.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points"
    assert JOKE.strip(), "joke is only whitespace"
    assert "\n" not in JOKE, "joke must land in one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)}-character joke to /output/entry.txt")


if __name__ == "__main__":
    main()
