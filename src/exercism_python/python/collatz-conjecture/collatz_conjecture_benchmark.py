import sys
import timeit

from functools import cache


def _is_even(number: int) -> bool:
    return number % 2 == 0


def _get_next_is_even(number: int) -> int:
    if _is_even(number):
        return number // 2

    return 3 * number + 1


def _steps_iter_nice_is_even(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        number = _get_next_is_even(number)
        steps += 1
    return steps


def _is_odd(number: int) -> bool:
    return bool(number % 2)


def _get_next_is_odd(number: int) -> int:
    if _is_odd(number):
        return 3 * number + 1

    return number // 2


def _steps_iter_nice_is_odd(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        number = _get_next_is_odd(number)
        steps += 1
    return steps


def _get_next_direct(number: int) -> int:
    if number % 2:
        return 3 * number + 1

    return number // 2


def _steps_iter_nice_next_direct(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        number = _get_next_direct(number)
        steps += 1
    return steps


def _steps_iter_ifcont(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        steps += 1
        if number % 2:
            number = 3 * number + 1
            continue
        number //= 2

    return steps


def _steps_iter_ifelse(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number //= 2
        steps += 1

    return steps


def _steps_iter_ternary(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    steps = 0
    while number > 1:
        number = (3 * number + 1) if number % 2 else (number // 2)
        steps += 1
    return steps


@cache
def _steps_recurse_cache(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    if number == 1:
        return 0

    if number % 2:
        return 1 + _steps_recurse_cache(3 * number + 1)

    return 1 + _steps_recurse_cache(number // 2)


def _steps_recurse_if(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    if number == 1:
        return 0

    if number % 2:
        return 1 + _steps_recurse_if(3 * number + 1)

    return 1 + _steps_recurse_if(number // 2)


def _steps_recurse_ternary(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    if number == 1:
        return 0

    return 1 + _steps_recurse_ternary((3 * number + 1) if number % 2 else (number // 2))


bench_functions = {
    'recursive with ternary': _steps_recurse_ternary,
    'recursive with if': _steps_recurse_if,
    'recursive with cache': _steps_recurse_cache,
    'iteration with ternary': _steps_iter_ternary,
    'iteration with if-else': _steps_iter_ifelse,
    'iteration with if-cont': _steps_iter_ifcont,
    'iteration with nice next direct': _steps_iter_nice_next_direct,
    'iteration with nice is even': _steps_iter_nice_is_even,
    'iteration with nice next is odd': _steps_iter_nice_is_odd,
}


def _pretty_print(start_n: int, stop_n: int, iterations: int, results: list[tuple]) -> None:
    """It prints pretty but code is kinda ugly.

    Should've imported some pretty print table lib.
    """

    c1_len = max(len(str(x[0])) for x in results)

    # padding for the "0."; so should be at least 2 ;)
    padding = 4

    c2_commas = 8
    c2_len = c2_commas + padding

    c3_commas = 8
    c3_len = c3_commas + padding

    header_row_format = f'| {{:{c1_len}}} | {{:{c2_len + 1}}} | {{:{c3_len + 1}}} |'
    result_row_format = (
        f'| {{:{c1_len}}} | {{:>{c2_len}.{c2_commas}f}}s | {{:>{c3_len}.{c3_commas}f}}s |'
    )
    divider = f'+-{"-" * c1_len}-+-{"-" * (c2_len + 1)}-+-{"-" * (c3_len + 1)}-+'
    param_padding = max(len(str(x)) for x in [start_n, stop_n, iterations])

    header_row = header_row_format.format(*['Description', 'Total', 'Mean'])
    result_rows = ''
    for result in results:
        result_rows += f'{result_row_format.format(*result)}\n'

    print(
        '\nParameters:\n'
        f'  start n:    {start_n:{param_padding}}\n'
        f'  stop n:     {stop_n:{param_padding}}\n'
        f'  iterations: {iterations:{param_padding}}\n'
        '\nBenchmark results:\n'
        f'{divider}\n'
        f'{header_row}\n'
        f'{divider}\n'
        f'{result_rows}'
        f'{divider}\n'
    )


def main() -> None:
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0].split('/')[-1]} <START_N> <STOP_N>')
        sys.exit(1)

    start_n = int(sys.argv[1])
    stop_n = int(sys.argv[2])
    step = 1 if stop_n >= start_n else -1

    results = []
    for description, steps in bench_functions.items():
        print(f'benchmarking "{description}"...')
        times = []
        for i in range(start_n, stop_n, step):
            starttime = timeit.default_timer()
            steps(i)
            times.append(timeit.default_timer() - starttime)

        sum_time = sum(times)
        mean_time = sum_time / len(times) if len(times) > 0 else 0
        results.append((description, sum_time, mean_time))

    results = sorted(results, key=lambda t: t[1])

    _pretty_print(start_n, stop_n, abs(stop_n - start_n), results)


if __name__ == '__main__':
    main()
