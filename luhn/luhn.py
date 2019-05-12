import re


class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def is_valid(self):
        if len(self.card_num) < 2 or re.search("\\D", self.card_num):
            return False

        card_num_list = [int(digit) for digit in self.card_num]
        card_num_list.reverse()
        for i in range(1, len(card_num_list), 2):
            value = card_num_list[i] * 2
            if value > 9:
                value -= 9
            card_num_list[i] = value

        return sum(card_num_list) % 10 == 0
