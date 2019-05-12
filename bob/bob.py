QUESTION = 'Sure.'
YELLING = 'Whoa, chill out!'
QUESTION_YELLING = "Calm down, I know what I'm doing!"
NOTHING = 'Fine. Be that way!'
WHATEVER = 'Whatever.'


def hey(phrase):
    phrase = phrase.strip()
    question = phrase.endswith("?")
    yelling = phrase.isupper()

    if question and yelling:
        return QUESTION_YELLING
    if question:
        return QUESTION
    if yelling:
        return YELLING
    if not phrase:
        return NOTHING

    return WHATEVER
