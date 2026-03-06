from greet import greet


def test_basic():
    assert greet("World") == "Hello, World!"


def test_empty():
    assert greet("") == "Hello, !"


def test_chinese():
    assert greet("小明") == "Hello, 小明!"
