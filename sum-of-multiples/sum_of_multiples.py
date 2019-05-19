def sum_of_multiples(limit, multiples):
    return sum(i for i in range(1, limit) if any((lambda x: x > 0 and i % x == 0)(x) for x in multiples))
