"""Entry for make.fun bounty u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.

Writes one single-line patch note for a bug in real life / human
biology to /output/entry.txt. Standard library only; deterministic:
the same line every run.

The bug: the brain replaying one song on loop at 3 a.m. with the
skip button removed — a specific, recognisable body bug, told in
the terse register of a real release note. The line is 106 chars,
well inside the 1-160 gate, with no padding: every word works.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where the brain replayed the same song on "
    "loop at 3 a.m. with the skip button removed."
)


def main():
    if not 1 <= len(LINE) <= 160:
        raise ValueError("entry line must be 1-160 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
