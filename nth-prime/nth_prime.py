from itertools import count

from math import sqrt


def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError("Argument must be a positive integer")

    counter = 0
    for i in count(start=2):
        if is_prime(i):
            counter += 1
            if counter == positive_number:
                return i


def is_prime(candidate):
    divisors = [i for i in range(2, int(sqrt(candidate)) + 1) if candidate % i == 0]
    return len(divisors) == 0
