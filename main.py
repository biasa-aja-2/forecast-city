"""Funniest Forecast for a City That Isn't.

The weather forecast for Grumblwick, a city that does not exist.

Why this line: flat bulletin phrasing that breaks with absurd weather
-- lost socks drizzle over the invented city Grumblwick -- with concrete
numbers (14 degrees, clearing by noon) and a deadpan kicker: umbrellas
useless, laundry baffled. The joke comes from the weather itself, not
from a pun bolted on, and the invented city feels like a place.
Pure stdlib, no network, no secrets.
"""

import os
import sys

LINE = "Forecast for Grumblwick: drizzle of lost socks at 14 degrees, clearing by noon; umbrellas useless, laundry baffled."
# One sentence only: the semicolon carries the second beat, so the gate's
# exactly-one-sentence rule still holds and the kicker stays at the end.


def validate(line):
    """Refuse any line that breaks the competition gate: 1-120 chars,
    single line, not whitespace-only, exactly one sentence."""
    if not (1 <= len(line) <= 120):
        sys.exit("gate failed: length %d not in 1..120" % len(line))
    if line.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("gate failed: line is not a single line")
    if line.count(".") != 1 or not line.endswith("."):
        sys.exit("gate failed: not exactly one sentence")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Self-check gate, factored out so main() stays short.
    validate(LINE)

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
