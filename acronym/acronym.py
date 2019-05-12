import re


def abbreviate(words):
    split = re.split("[^a-zA-Z']+", words)
    return "".join(word.upper()[0] for word in split)
