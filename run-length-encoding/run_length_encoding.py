def decode(string: str) -> str:
    numbers = []
    chars = []
    num = ""

    for c in string:
        if c.isdigit():
            num += c
        else:
            if len(num) == 0:
                numbers.append(1)
            else:
                numbers.append(int(num))
            chars.append(c)
            num = ""

    return "".join(chars[i] * numbers[i] for i in range(0, len(numbers)))


def encode(string: str) -> str:
    curr_char = ""
    counter = 0
    result = ""

    for char in string:
        if len(curr_char) == 0:
            curr_char = char
        if char != curr_char:
            if counter > 1:
                result += str(counter)
            result += curr_char
            curr_char = char
            counter = 1
        else:
            counter += 1

    if counter > 1:
        result += str(counter)
    result += curr_char

    return result
