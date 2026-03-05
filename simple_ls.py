#!/usr/bin/env python3
"""A minimal Python implementation of `ls`."""

from __future__ import annotations

import os
import sys


def main() -> int:
    target = sys.argv[1] if len(sys.argv) > 1 else "."

    try:
        entries = sorted(os.listdir(target))
    except OSError as exc:
        print(f"simple_ls.py: cannot access '{target}': {exc.strerror}", file=sys.stderr)
        return 1

    for entry in entries:
        print(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
