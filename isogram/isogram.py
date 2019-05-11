import re


def is_isogram(string):
    sanitized_input = re.sub("[^a-z]", "", string.lower())
    return len(sanitized_input) == len(set(sanitized_input))
