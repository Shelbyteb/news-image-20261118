#!/usr/bin/env python3
"""Entry program for news-image-20261118.

Copies the composed front page, entry.png, sitting beside this file
into the output directory make.fun provides, so the grader sees the
same bytes on every run. Standard library only; no network, no
arguments. The output directory comes from MAKEFUN_OUTPUT_DIR, or
defaults to /output.
"""

import os
import shutil
import sys

ENTRY = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY)
    if not os.path.isfile(source):
        print(f"error: {ENTRY} is missing next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, ENTRY)
    shutil.copyfile(source, target)
    copied = os.path.getsize(target)
    expected = os.path.getsize(source)
    if copied != expected:
        print(f"error: copied {copied} bytes, expected {expected}",
              file=sys.stderr)
        return 1
    print("wrote", target, copied, "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
