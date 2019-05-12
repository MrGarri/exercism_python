import re


def word_count(phrase):
    sanitized_input = re.sub("[^0-9a-z']", " ", phrase.lower())
    split = sanitized_input.split()
    result = dict()

    for word in split:
        word = word.strip("\'")
        result[word] = result.setdefault(word, 0) + 1

    return result
