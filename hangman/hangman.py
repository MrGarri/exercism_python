# Game status categories
# Change the values as you see fit
import re

STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word: str):
        self.__word = word
        self.remaining_guesses = 9
        self.__status = STATUS_ONGOING
        self.__masked_word = ['_'] * len(word)

    def guess(self, char: chr):
        if self.__status == STATUS_LOSE:
            raise ValueError("You ran out of guesses!")
        if self.__status == STATUS_WIN:
            raise ValueError("You've already won!")

        if char in self.__word and char not in self.__masked_word:
            matches = [m.start() for m in re.finditer(char, self.__word)]
            for i in matches:
                self.__masked_word[i] = self.__word[i]
        else:
            self.remaining_guesses -= 1

        if self.get_masked_word() == self.__word:
            self.__status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.__status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.__masked_word)

    def get_status(self):
        return self.__status
