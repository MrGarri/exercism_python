from functools import reduce


def largest_product(series: str, size: int) -> int:

    if size == 0:
        return 1
    if len(series) < size:
        raise ValueError("Size cannot be greater than series length")
    if len(series) <= 0:
        raise ValueError("Series cannot be empty")
    if size < 0:
        raise ValueError("Size must be a positive integer")
    if not series.isdigit():
        raise ValueError("Series must contain only numbers")

    windows = [series[i:i+size] for i in range(0, len(series) - size + 1)]
    return max(reduce((lambda x, y: x*y), map(int, str(x))) for x in windows)
