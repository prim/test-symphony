from fizzbuzz import fizzbuzz


def test_basic():
    result = fizzbuzz(15)
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_fizz_at_6():
    result = fizzbuzz(6)
    assert result[5] == "Fizz"


def test_buzz_at_10():
    result = fizzbuzz(10)
    assert result[9] == "Buzz"


def test_one():
    result = fizzbuzz(1)
    assert result == ["1"]


def test_negative():
    result = fizzbuzz(-1)
    assert result == []


def test_numeric_string_at_14():
    result = fizzbuzz(14)
    assert result[13] == "14"


def test_full_15():
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "Fourteen", "FizzBuzz"
    ]
    assert fizzbuzz(15) == expected
