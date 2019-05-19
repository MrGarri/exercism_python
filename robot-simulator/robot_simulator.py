# Globals for the bearings
# Change the values as you see fit
NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return self.x, self.y

    def turn_right(self):
        x, y = self.bearing
        self.bearing = y, -x

    def turn_left(self):
        x, y = self.bearing
        self.bearing = -y, x

    def advance(self):
        x, y = self.bearing
        self.x += x
        self.y += y

    def simulate(self, instructions: str):
        movements = {
            "R": self.turn_right,
            "L": self.turn_left,
            "A": self.advance
        }

        for instruction in instructions:
            movements[instruction]()




