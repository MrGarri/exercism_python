vowels = ('a', 'e', 'i', 'o', 'u')


def translate(text):
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    if word.startswith(vowels + ('xr', 'yt')):
        return word + 'ay'
    elif len(word) == 2 and word[1] == 'y':
        return word[::-1] + 'ay'
    elif word.startswith('qu'):
        return translate_word(word[2::] + word[0:2])
    else:
        return translate_word(word[1::] + word[0])
