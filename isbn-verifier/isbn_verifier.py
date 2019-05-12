import re


def verify(isbn):
    sanitized_isbn = re.sub("[^0-9X]", "", isbn)
    if len(sanitized_isbn) != 10 or ("X" in sanitized_isbn and not sanitized_isbn.endswith("X")):
        return False

    sum_of_digits = 0
    multiplier = 10
    for digit in sanitized_isbn:
        if digit == "X":
            digit = "10"
        sum_of_digits += multiplier * int(digit)
        multiplier -= 1

    return sum_of_digits % 11 == 0
