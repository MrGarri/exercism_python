from collections import Iterable


def flatten(iterable: Iterable):
    result = []

    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            result += flatten(item)
        elif item is not None:
            result.append(item)

    return result
