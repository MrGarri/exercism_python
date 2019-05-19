EARTH_ORBITAL_PERIOD = 31557600

ON_MERCURY = 0.2408467
ON_VENUS = 0.61529726
ON_MARS = 1.8808158
ON_JUPITER = 11.862615
ON_SATURN = 29.447498
ON_URANUS = 84.016846
ON_NEPTUNE = 164.79132


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / EARTH_ORBITAL_PERIOD, 2)

    def on_mercury(self):
        return round(self.on_earth() / ON_MERCURY, 2)

    def on_venus(self):
        return round(self.on_earth() / ON_VENUS, 2)

    def on_mars(self):
        return round(self.on_earth() / ON_MARS, 2)

    def on_jupiter(self):
        return round(self.on_earth() / ON_JUPITER, 2)

    def on_saturn(self):
        return round(self.on_earth() / ON_SATURN, 2)

    def on_uranus(self):
        return round(self.on_earth() / ON_URANUS, 2)

    def on_neptune(self):
        return round(self.on_earth() / ON_NEPTUNE, 2)
