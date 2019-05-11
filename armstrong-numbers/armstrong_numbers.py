def is_armstrong_number(number):
    number_to_string = str(number)
    power = len(number_to_string)

    result = sum(int(c)**power for c in number_to_string)

    return result == number
