from typing import List


def slices(series: str, length: int) -> List[str]:
    if length <= 0:
        raise ValueError("Length cannot be negative.")

    len_series: int = len(series)

    if length > len_series:
        raise ValueError("Length cannot be bigger than actual series.")

    # Solution "borrowed" from other solutions:
    # return [series[i:length + i] for i in range(len_series - length + 1)]

    return [series[i:length + i] for i in range(len_series) if length + i <= len_series]
