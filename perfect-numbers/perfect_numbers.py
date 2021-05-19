from functools import reduce

def factors_with_reduce(n):
    return set(reduce(list.__add__,
                ([i, n//i if i != 1 else i] for i in range(1, min(int(n**0.5) + 1, n)) if not n % i), []))


def factors_with_sum(n):
    return set(sum(([i, n//i if i != 1 else i] for i in range(1, min(int(n**0.5) + 1, n)) if not n % i), []))


def classify(number):
    if number <= 0:
        raise ValueError("Please specify a positive integer.")

    # My original solution which takes around 5-6s:
    # Note: "not number % i" seems to be faster than "number % i == 0" (6s vs 5s)
    aliquot_sum = sum(i for i in range(1, number) if not number % i)

    # Solutions based on https://stackoverflow.com/a/6800214 which take around 0.05s:
    # aliquot_sum = sum(factors_with_reduce(number))
    # aliquot_sum = sum(factors_with_sum(number))

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
