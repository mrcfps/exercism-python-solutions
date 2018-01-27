def slices(series, length):
    if len(series) < length:
        raise ValueError("overly long length")
    elif length == 0:
        raise ValueError("length cannot be 0")
    return [list(int(digit) for digit in series[start:start+length])
            for start in range(len(series) - length + 1)]
