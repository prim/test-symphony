#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence, TextIO


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple Python implementation of ls.")
    parser.add_argument(
        "paths",
        metavar="path",
        nargs="*",
        default=["."],
        help="Paths to list. Defaults to the current directory.",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Do not ignore entries starting with .",
    )
    return parser


def list_path(path: Path, include_hidden: bool = False) -> list[str]:
    if path.is_dir():
        entries = [
            entry.name
            for entry in path.iterdir()
            if include_hidden or not entry.name.startswith(".")
        ]
        return sorted(entries)
    if path.exists():
        return [path.name]
    raise FileNotFoundError(path)


def write_listing(
    raw_paths: Sequence[str],
    include_hidden: bool,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    exit_code = 0
    show_headers = len(raw_paths) > 1

    for index, raw_path in enumerate(raw_paths):
        path = Path(raw_path)

        try:
            entries = list_path(path, include_hidden=include_hidden)
        except FileNotFoundError:
            print(f"ls.py: cannot access '{raw_path}': No such file or directory", file=stderr)
            exit_code = 1
            continue

        if show_headers:
            if index:
                print(file=stdout)
            print(f"{raw_path}:", file=stdout)

        for entry in entries:
            print(entry, file=stdout)

    return exit_code


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return write_listing(args.paths, include_hidden=args.all, stdout=sys.stdout, stderr=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
