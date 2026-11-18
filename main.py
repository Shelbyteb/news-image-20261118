#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261118.

The entry image is composed ahead of time (see compose.py) and shipped
in this repository as entry.png. This program simply copies it to the
output directory, so both graded runs write identical bytes.

Standard library only; no network access.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
