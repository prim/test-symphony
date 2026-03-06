import pytest

from date_range import date_range


def test_includes_both_endpoints_for_default_step():
    assert date_range("2024-01-01", "2024-01-03") == [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
    ]


def test_step_parameter_advances_by_multiple_days():
    assert date_range("2024-01-01", "2024-01-07", 2) == [
        "2024-01-01",
        "2024-01-03",
        "2024-01-05",
        "2024-01-07",
    ]


def test_descending_range_uses_positive_step():
    assert date_range("2024-01-05", "2024-01-01", 2) == [
        "2024-01-05",
        "2024-01-03",
        "2024-01-01",
    ]


@pytest.mark.parametrize("step", [0, -1])
def test_non_positive_step_raises_value_error(step: int):
    with pytest.raises(ValueError, match="step must be positive"):
        date_range("2024-01-01", "2024-01-02", step)


@pytest.mark.parametrize("value", ["2024/01/01", "2024-13-01", "2023-02-29"])
def test_invalid_start_date_mentions_bad_value(value: str):
    with pytest.raises(ValueError, match=value):
        date_range(value, "2024-03-01")


def test_invalid_end_date_mentions_bad_value():
    with pytest.raises(ValueError, match="2024-02-30"):
        date_range("2024-02-01", "2024-02-30")


def test_leap_day_is_valid_in_leap_year():
    assert date_range("2024-02-28", "2024-03-01") == [
        "2024-02-28",
        "2024-02-29",
        "2024-03-01",
    ]


def test_cross_year_range_is_supported():
    assert date_range("2023-12-30", "2024-01-02") == [
        "2023-12-30",
        "2023-12-31",
        "2024-01-01",
        "2024-01-02",
    ]


def test_same_start_and_end_returns_single_value():
    assert date_range("2024-01-01", "2024-01-01") == ["2024-01-01"]


def test_step_larger_than_span_returns_only_start():
    assert date_range("2024-01-01", "2024-01-03", 5) == ["2024-01-01"]


def test_cross_month_boundary_is_supported():
    assert date_range("2024-01-31", "2024-02-02") == [
        "2024-01-31",
        "2024-02-01",
        "2024-02-02",
    ]


def test_large_step_can_skip_end_when_not_landed_on_exactly():
    assert date_range("2024-01-01", "2024-01-10", 4) == [
        "2024-01-01",
        "2024-01-05",
        "2024-01-09",
    ]
