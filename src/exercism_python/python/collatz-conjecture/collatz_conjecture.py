def _is_even(number: int) -> bool:
    return number % 2 == 0


def _get_next(number: int) -> int:
    """Get the next number of the Collatz Conjecture.

    :param number: int - the current number.
    :return: int - if `number` is even, the `number` divided by 2, or otherwise "3 * `number` + 1".
    """
    if _is_even(number):
        return number // 2

    return 3 * number + 1


def steps(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        number = _get_next(number)
        steps += 1

    return steps
