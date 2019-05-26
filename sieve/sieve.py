from math import sqrt


def sieve(limit):
    return [i for i in range(2, limit + 1) if is_prime(i)]


def is_prime(candidate):
    divisors = [i for i in range(2, int(sqrt(candidate)) + 1) if candidate % i == 0]
    return len(divisors) == 0
