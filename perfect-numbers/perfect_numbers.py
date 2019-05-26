def classify(number):
    if number < 1:
        raise ValueError("Number must be a positive integer.")

    if aliquot_sum(number) == number:
        return "perfect"
    elif aliquot_sum(number) < number:
        return "deficient"
    else:
        return "abundant"


def aliquot_sum(number):
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0)
