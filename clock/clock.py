class Clock(object):
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        if total_minutes < 0:
            total_minutes += 60 * 24 * (1 + int(60 / -1*total_minutes / 24))

        self.minute = total_minutes % 60
        self.hour = int(total_minutes / 60) % 24

    def __repr__(self):
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other: "Clock") -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes) -> "Clock":
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes) -> "Clock":
        return Clock(self.hour, self.minute - minutes)
