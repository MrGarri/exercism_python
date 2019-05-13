def YACHT(dice):
    return 50 if len(set(dice)) == 1 else 0


def ONES(dice):
    return calculate_ns(dice, 1)


def TWOS(dice):
    return calculate_ns(dice, 2)


def THREES(dice):
    return calculate_ns(dice, 3)


def FOURS(dice):
    return calculate_ns(dice, 4)


def FIVES(dice):
    return calculate_ns(dice, 5)


def SIXES(dice):
    return calculate_ns(dice, 6)


def FULL_HOUSE(dice):
    if len(set(dice)) != 2:
        return 0
    if dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3:
        return sum(dice)
    else:
        return 0


def FOUR_OF_A_KIND(dice):
    return sum(value * 4 for value in set(dice) if dice.count(value) >= 4)


def LITTLE_STRAIGHT(dice):
    return 30 if {1, 2, 3, 4, 5} <= set(dice) else 0


def BIG_STRAIGHT(dice):
    return 30 if {2, 3, 4, 5, 6} == set(dice) else 0


def CHOICE(dice):
    return sum(dice)


def score(dice, category):
    return category(dice)


def calculate_ns(dice, value):
    return dice.count(value) * value
