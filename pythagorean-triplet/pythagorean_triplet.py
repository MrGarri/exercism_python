def triplets_with_sum(sum_of_triplet):
    return set(triplet for triplet in triplets_in_range(3, sum_of_triplet) if is_triplet(triplet))


def triplets_in_range(range_start, range_end):
    for a in range(range_start, range_end // 2):
        for b in range(a + 1, range_end // 2):
            c = range_end - b - a
            if c > b > a:
                yield a, b, c


def is_triplet(triplet):
    a, b, c = triplet
    return pow(a, 2) + pow(b, 2) == pow(c, 2)
