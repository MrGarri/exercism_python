import re


def is_pangram(sentence):
    letters = re.sub('[^a-zA-Z]', '', sentence).lower()
    return len(set(letters)) == 26
