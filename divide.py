"""Simple division helper."""


def divide(a, b):
    """Return the result of dividing ``a`` by ``b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
