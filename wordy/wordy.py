import sys


def calculate(question: str) -> int:
    words = question[8:-1].split()

    try:
        result = int(words.pop(0))
    except IndexError:
        raise ValueError("Error")

    while words:
        operand = words.pop(0)

        try:
            if operand == "plus":
                try:
                    num = words.pop(0)
                except IndexError:
                    raise ValueError("Missing operand")
                result += int(num)
            elif operand == "minus":
                result -= int(words.pop(0))
            elif operand == "multiplied":
                words.pop(0)
                result *= int(words.pop(0))
            elif operand == "divided":
                words.pop(0)
                result /= int(words.pop(0))
            else:
                raise ValueError("Unsupported mathematical operatin")
        except ValueError:
            print("Some error occured", file=sys.stderr)
            raise

    return result
