# Other solutions: https://exercism.io/tracks/python/exercises/armstrong-numbers/solutions/d5c70aa00fe64b5fbc8e7b7a0fa1e117#solution-comment-172058

def is_armstrong_number(number: str) -> bool:
    digits: str = str(number)
    len_digits: int = len(digits)

    # Inspired by other solutions:
    # return number == sum(int(d) ** len_digits for d in digits)
    # return number == sum(list(map(lambda d: int(d) ** len_digits, digits)))

    # My original:
    return number == sum(map(pow, map(int, digits), [len_digits] * len_digits))
