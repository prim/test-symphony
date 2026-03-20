from __future__ import annotations

from datetime import date, timedelta
import re


_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")


def _parse_date(value: str) -> date:
    if not _DATE_PATTERN.fullmatch(value):
        raise ValueError(f"invalid date: {value}")

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"invalid date: {value}") from exc


def date_range(start: str, end: str, step: int = 1) -> list[str]:
    if step <= 0:
        raise ValueError("step must be positive")

    start_date = _parse_date(start)
    end_date = _parse_date(end)

    if start_date == end_date:
        return [start_date.isoformat()]

    direction = 1 if start_date < end_date else -1
    delta = timedelta(days=step * direction)
    result: list[str] = []
    current = start_date

    while (direction == 1 and current <= end_date) or (
        direction == -1 and current >= end_date
    ):
        result.append(current.isoformat())
        current += delta

    return result
