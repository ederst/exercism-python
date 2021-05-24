from typing import List


def slices(series: str, length: int) -> List[str]:
    if length <= 0:
        raise ValueError("Length cannot be negative.")

    len_series: int = len(series)

    if length > len_series:
        raise ValueError("Length cannot be bigger than actual series.")

    return [series[i:length + i] for i in range(len(series)) if length + i <= len_series]
