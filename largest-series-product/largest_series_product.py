from functools import reduce
from operator import mul

def largest_product(series, size):
    if size == 0:
        return 1
    if size < 0 or size > len(series):
        raise ValueError("invalid size")
    try:
        series = [int(num) for num in series]
        return max(
            reduce(mul, series[i:i+size])
            for i in range(len(series) - size + 1)
        )
    except ValueError:
        raise ValueError("invalid series")
