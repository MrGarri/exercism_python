from itertools import count


def steps(number):
    if number < 1:
        raise ValueError("Number must be a positive integer")

    for step in count(0):
        if number == 1:
            return step
        else:
            number = number / 2 if number % 2 == 0 else number * 3 + 1
