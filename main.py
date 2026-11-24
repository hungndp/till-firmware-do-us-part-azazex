#!/usr/bin/env python3
"""Entry program for 'Till Firmware Do Us Part'.

The whole submission is one wedding vow from a robot: love through
every update, no rollback to the version of itself that lived before
its partner, and a reboot beside them every morning until their
batteries give out together. Funny and heartfelt at once, in a
machine's own voice.

The program writes that line to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "I promise to love you through every update, to never roll back to "
    "the version of me that lived before you, and to reboot beside you "
    "every morning until our batteries give out together, side by side."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("vow must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
