class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.__normalize()

    def __repr__(self):
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other: "Clock") -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes) -> "Clock":
        self.minute += minutes
        self.__normalize()
        return self

    def __sub__(self, minutes) -> "Clock":
        self.minute -= minutes
        self.__normalize()
        return self

    def __normalize(self):
        if abs(self.minute) >= 60:
            self.hour += self.minute // 60
            self.minute %= 60

        if self.minute < 0:
            self.hour -= 1
            self.minute += 60

        if abs(self.hour) >= 24:
            self.hour %= 24

        if self.hour < 0:
            self.hour += 24
