from itertools import dropwhile
from random import choice
from string import ascii_uppercase as letters, digits


class Robot(object):

    used_names = set()

    def __init__(self):
        self.reset()

    @staticmethod
    def generate_random_names():
        while True:
            names = [letters] * 2 + [digits] * 3
            yield "".join(
                choice(name)
                for name in names
            )

    def _get_name_used(self, name):
        return name in self.used_names

    def get_random_name(self):
        names = Robot.generate_random_names()
        return next(dropwhile(self._get_name_used, names))

    def reset(self):
        self.name = self.get_random_name()
        self.used_names.add(self.name)
