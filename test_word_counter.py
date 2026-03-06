import pytest

from word_counter import count_words


def test_counts_words_case_insensitively() -> None:
    assert count_words("Hello hello HELLO world") == {"hello": 3, "world": 1}


def test_removes_supported_punctuation() -> None:
    text = 'Hello, world. Hello! "World"; hello: world?'

    assert count_words(text) == {"hello": 3, "world": 3}


def test_supports_multiline_text() -> None:
    text = "One fish\nTwo fish\nred fish\nblue fish"

    assert count_words(text) == {"one": 1, "two": 1, "red": 1, "blue": 1, "fish": 4}


def test_returns_empty_dict_for_empty_string() -> None:
    assert count_words("") == {}


def test_returns_empty_dict_for_whitespace_only_text() -> None:
    assert count_words("  \n\t  ") == {}


@pytest.mark.parametrize("invalid_value", [None, 123, ["hello"], {"text": "hello"}])
def test_raises_type_error_for_non_string_input(invalid_value: object) -> None:
    with pytest.raises(TypeError):
        count_words(invalid_value)  # type: ignore[arg-type]


def test_removes_single_quotes_from_words() -> None:
    assert count_words("It's it's ITS") == {"its": 3}
