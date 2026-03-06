import pytest

from csv_parser import parse_csv


def test_parses_basic_csv_rows_into_dicts():
    text = 'name,age\nAlice,30\nBob,25'

    assert parse_csv(text) == [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
    ]


def test_supports_quoted_fields_with_commas():
    text = 'message,count\n"hello, world",1'

    assert parse_csv(text) == [{'message': 'hello, world', 'count': '1'}]


def test_supports_escaped_quotes_inside_quoted_fields():
    text = 'quote\n"say ""hi"""'

    assert parse_csv(text) == [{'quote': 'say "hi"'}]


def test_trims_unquoted_fields_but_preserves_spaces_inside_quotes():
    text = 'left,right\n hello , " hello " '

    assert parse_csv(text) == [{'left': 'hello', 'right': ' hello '}]


def test_skips_blank_lines():
    text = 'name,age\n\nAlice,30\n   \nBob,25\n'

    assert parse_csv(text) == [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
    ]


def test_raises_value_error_with_line_number_for_mismatched_fields():
    text = 'name,age\nAlice,30\nBob'

    with pytest.raises(ValueError, match='Line 3: expected 2 fields, got 1'):
        parse_csv(text)


def test_raises_type_error_for_non_string_input():
    with pytest.raises(TypeError, match='text must be a string'):
        parse_csv(None)


def test_returns_empty_list_for_empty_string():
    assert parse_csv('') == []


def test_returns_empty_list_when_only_header_exists():
    assert parse_csv('name,age') == []


def test_supports_windows_newlines():
    text = 'name,age\r\nAlice,30\r\nBob,25'

    assert parse_csv(text) == [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
    ]
