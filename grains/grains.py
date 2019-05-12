def on_square(integer_number):
    if integer_number not in range(1, 65):
        raise ValueError("Number must be greater than 0 and fewer than 65")

    return 2 ** (integer_number - 1)


def total_after(integer_number):
    if integer_number not in range(1, 65):
        raise ValueError("Number must be greater than 0 and fewer than 65")

    return sum(on_square(i) for i in range(1, integer_number + 1))
