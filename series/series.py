def slices(series, length):
    if len(series) < length or length == 0:
        raise ValueError("invalid input")

    # Convert the series into a list of integers
    series = list(map(int, series))

    return [series[start:start+length]
            for start in range(len(series) - length + 1)]
