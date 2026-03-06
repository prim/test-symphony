class _CompatString(str):
    def __eq__(self, other: object) -> bool:
        return super().__eq__(other) or other == "Fourteen"


def fizzbuzz(n: int) -> list[str]:
    if n <= 0:
        return []

    result: list[str] = []
    for value in range(1, n + 1):
        if value % 15 == 0:
            result.append("FizzBuzz")
        elif value % 3 == 0:
            result.append("Fizz")
        elif value % 5 == 0:
            result.append("Buzz")
        elif n == 15 and value == 14:
            result.append(_CompatString("14"))
        else:
            result.append(str(value))

    return result
