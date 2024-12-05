def _steps(number: int) -> int:
    if number == 1:
        return 0

    if number % 2:
        return 1 + _steps(3 * number + 1)

    return 1 + _steps(number // 2)


def steps(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    return _steps(number)
