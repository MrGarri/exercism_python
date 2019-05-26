import random

from math import floor


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        throws = [random.randint(1, 6) for _ in range(4)]
        throws.sort(reverse=True)
        return sum(throws[0:3])


def modifier(constitution: int):
    return floor((constitution - 10) / 2)
