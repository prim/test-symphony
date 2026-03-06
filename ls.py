#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable, Sequence, TextIO


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple Python implementation of ls.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to list")
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Do not ignore entries starting with .",
    )
    return parser


def list_directory(path: Path, show_all: bool) -> list[str]:
    names = [entry.name for entry in path.iterdir() if show_all or not entry.name.startswith(".")]
    names = sorted(names)

    if show_all:
        return [".", "..", *names]

    return names


def render_directory(label: str, entries: Iterable[str], show_header: bool) -> str:
    body = "\n".join(entries)
    if not show_header:
        return body
    if body:
        return f"{label}:\n{body}"
    return f"{label}:"


def render_sections(sections: Sequence[tuple[str, str]]) -> str:
    parts: list[str] = []
    previous_kind: str | None = None

    for kind, content in sections:
        if not content:
            continue

        if parts:
            separator = "\n" if kind == "file" and previous_kind == "file" else "\n\n"
            parts.append(separator)

        parts.append(content)
        previous_kind = kind

    return "".join(parts)


def render_targets(paths: Sequence[str], show_all: bool, err: TextIO) -> int:
    show_headers = len(paths) > 1
    sections: list[tuple[str, str]] = []
    exit_code = 0

    for raw_path in paths:
        path = Path(raw_path)

        try:
            if path.is_dir():
                entries = list_directory(path, show_all)
                section = render_directory(raw_path, entries, show_headers)
                if section:
                    sections.append(("directory", section))
                continue

            if os.path.lexists(raw_path):
                sections.append(("file", raw_path))
                continue

            raise FileNotFoundError
        except OSError as exc:
            message = "No such file or directory" if isinstance(exc, FileNotFoundError) else exc.strerror or str(exc)
            print(f"ls.py: cannot access '{raw_path}': {message}", file=err)
            exit_code = 1

    output = render_sections(sections)
    if output:
        sys.stdout.write(output)
        sys.stdout.write("\n")

    return exit_code


def main(argv: Sequence[str] | None = None, err: TextIO | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return render_targets(args.paths, show_all=args.all, err=err or sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
