"""Snooze Button Roast — make.fun entry.

Writes one roast line to /output/entry.txt: a single line of at most
200 characters roasting an alarm clock that rings at 6 AM on a Saturday.
"""

import hashlib
import os
import sys

# The entry: one line, fresh angle (a rooster that got promoted),
# punchline lands in the last few words. Exactly 140 characters,
# well inside the 200-character gate, so it is sayable in one breath.
ENTRY = (
    "My alarm clock rang at 6 AM on a Saturday like a rooster that got "
    "a promotion, a megaphone, and a grudge against everyone who ever slept in."
)

MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, in a single line.
    """
    problems = []
    if not text or not text.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in text.strip():
        problems.append("entry must be a single line")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not valid UTF-8: %s" % exc)
    return problems


def output_path():
    """Resolve where entry.txt goes: the harness sets MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path=None):
    """Validate the entry, then write it (no trailing newline) and report."""
    problems = validate_entry(text)
    if problems:
        for problem in problems:
            print("INVALID: %s" % problem, file=sys.stderr)
        sys.exit(1)
    target = path or output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("wrote %s (%d chars, sha256 %s)" % (target, len(text), digest))
    return target


def self_test():
    """Self-test: the entry passes the gate, and a too-long line fails it."""
    assert validate_entry(ENTRY) == [], "entry should pass the gate"
    assert len(ENTRY) <= MAX_CHARS, "entry over the char limit"
    assert validate_entry("x" * (MAX_CHARS + 1)), "over-long line must fail"
    assert validate_entry("   "), "blank line must fail"
    assert validate_entry("one\ntwo"), "multi-line text must fail"
    print("self-test passed: entry is %d chars" % len(ENTRY))


if __name__ == "__main__":
    self_test()
    write_entry(ENTRY)
