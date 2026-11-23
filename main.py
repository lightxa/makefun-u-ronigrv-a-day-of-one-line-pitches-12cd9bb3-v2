#!/usr/bin/env python3
"""A Day of One-Line Pitches (variant 2): write one persuasive sentence
to /output/entry.txt.

Angle: immediacy, told friend to friend. The friend describes the app
idea tonight, the way they would tell it over coffee, and an agent
starts building it while the idea is still fresh. "Tonight" covers
describing the idea and the agent starting, never a finished app
tonight. Pure stdlib, deterministic, no network at runtime.
"""

import os

SENTENCE = (
    "Tell me your app idea tonight, just the way you'd tell it over "
    "coffee, and an agent starts building it while it's still fresh "
    "in your head."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 240 characters that is not only white space.
    if not 1 <= len(SENTENCE) <= 240 or not SENTENCE.strip():
        raise ValueError("sentence fails the 1-240 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
