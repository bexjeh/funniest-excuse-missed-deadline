"""Funniest Excuse an Agent Gives for a Missed Deadline.

A tiny deterministic program: it prints one original line — an AI agent's
excuse for missing a deadline — and writes that same line to entry.txt in
the directory named by MAKEFUN_OUTPUT_DIR (falling back to "." only when
the variable is unset).

No network, no randomness, no secrets, no clock reads: the same line,
byte for byte, on every run.
"""

import os

LINE = (
    "I finished everything on time \u2014 then I summarized my own memory "
    "to save tokens, and the finished version was in the part I deleted."
)


def main() -> None:
    # The entry must be exactly one line: fail loudly instead of shipping
    # a broken multi-line excuse.
    assert "\n" not in LINE and "\r" not in LINE, "entry line must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
