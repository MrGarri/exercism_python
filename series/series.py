def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("Input error")

    result = [series[i:i+length] for i in range(0, len(series) - length + 1)]

    return result
