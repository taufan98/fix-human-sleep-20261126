#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun bounty entry.

Writes one line to /output/entry.txt: a changelog patch note announcing
that human sleep is fixed, with the joke carried by the side effect
(dreams in 4K) and the known issue (Mondays still exist).
"""

import os

ENTRY = 'v2.6.1 — Fixed: humans can now sleep through the night. Side effect: dreams now render in 4K. Known issue: Mondays still exist.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
