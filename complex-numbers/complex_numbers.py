from math import sqrt, exp, cos, sin


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: "ComplexNumber"):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other: "ComplexNumber"):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )

    def __sub__(self, other: "ComplexNumber"):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __truediv__(self, other: "ComplexNumber"):
        other_square = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / other_square,
            (self.imaginary * other.real - self.real * other.imaginary) / other_square
        )

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
            exp(self.real) * cos(self.imaginary),
            exp(self.real) * sin(self.imaginary)
        )

    def __eq__(self, other: "ComplexNumber"):
        return self.real == other.real and self.imaginary == other.imaginary
