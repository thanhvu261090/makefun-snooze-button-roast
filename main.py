#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one roast line to /output/entry.txt: an alarm clock that rings
at 6 AM on a Saturday, imagined as a rooster with a promotion.
"""

import os

# The entry, exactly 140 characters: one line, no trailing newline.
LINE = (
    "My alarm clock rang at 6 AM on a Saturday like a rooster that got "
    "a promotion, a megaphone, and a grudge against everyone who ever slept in."
)


def render_entry():
    """Return the entry line, checked against the 1-200 char gate."""
    if not LINE.strip() or "\n" in LINE or len(LINE) > 200:
        raise ValueError("entry fails the gate: must be one line, 1-200 chars")
    return LINE


def write_entry():
    """Write the entry byte-identical to /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(render_entry())
    print("wrote %s (%d chars)" % (path, len(LINE)))


if __name__ == "__main__":
    write_entry()
