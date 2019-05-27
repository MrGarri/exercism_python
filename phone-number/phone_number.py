import re


class Phone(object):
    def __init__(self, phone_number):
        tmp = ''.join(filter(lambda c: str.isdigit(c), phone_number))

        if len(tmp) != 10 and len(tmp) != 11:
            raise ValueError("Incorrect number length")
        elif len(tmp) == 11:
            if tmp[0] != '1':
                raise ValueError("Incorrect number")
            else:
                self.number = self.__get_number(tmp)
        else:
            self.number = self.__get_number(tmp)

    def pretty(self):
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'

    def __get_number(self, number):
        if len(number) == 11:
            number = number[1::]

        area_code = number[:3]
        exchange_code = number[3:6]

        if area_code[0] not in '23456789' or exchange_code[0] not in '23456789':
            raise ValueError("Incorrect number")

        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber_number = number[6:]
        return number
