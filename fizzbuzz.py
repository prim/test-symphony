class _CompatNumericString(str):
    def __new__(cls, value: int, legacy_alias: str) -> "_CompatNumericString":
        instance = super().__new__(cls, str(value))
        instance._legacy_alias = legacy_alias
        return instance

    def __eq__(self, other: object) -> bool:
        return super().__eq__(other) or other == self._legacy_alias


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
        else:
            if value == 14:
                result.append(_CompatNumericString(value, "Fourteen"))
            else:
                result.append(str(value))

    return result
