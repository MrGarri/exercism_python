class Queen(object):
    def __init__(self, row, column):
        if any(pos < 0 or pos > 7 for pos in (row, column)):
            raise ValueError("Invalid queen position")

        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def can_attack(self, another_queen):
        if self == another_queen:
            raise ValueError("Queens cannot occupy the same position.")

        return self.row == another_queen.row \
               or self.column == another_queen.column \
               or abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
