def append(xs, ys):
    return xs + ys


def concat(lists):
    result = []
    for element in lists:
        result += element

    return result


def filter_clone(function, xs):
    return [element for element in xs if function(element) is True]


def length(xs):
    return sum(1 for _ in xs)


def map_clone(function, xs):
    return [function(element) for element in xs]


def foldl(function, xs, acc):
    result = acc
    for element in xs:
        result = function(result, element)

    return result


def foldr(function, xs, acc):
    result = acc
    for element in xs[::-1]:
        result = function(element, result)

    return result


def reverse(xs):
    result = []
    for element in xs:
        result.insert(0, element)

    return result
