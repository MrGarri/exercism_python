def prime_factors(natural_number):
    factors = []
    candidate = 2
    while natural_number > 1 or candidate <= natural_number / 2:
        if natural_number % candidate == 0:
            factors.append(candidate)
            natural_number /= candidate
        else:
            candidate += 1

    return factors
