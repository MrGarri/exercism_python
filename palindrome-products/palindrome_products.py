def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be greater than max_factor")
    if max_factor == min_factor:
        return None, []

    palindromes = get_palindromes(min_factor, max_factor + 1)
    largest = max(palindromes)
    return largest, palindromes[largest]


def smallest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be greater than max_factor")
    if max_factor - min_factor < 2:
        return None, []

    palindromes = get_palindromes(min_factor, max_factor + 1)
    smallest = min(palindromes)
    return smallest, palindromes[smallest]


def get_palindromes(start, end):
    palindromes = {}
    for i in range(start, end):
        for j in range(i, end):
            prod = i * j
            if is_palindrome(prod):
                palindromes.setdefault(prod, []).append((i, j))

    return palindromes


def is_palindrome(number: int):
    return str(number) == str(number)[::-1]
