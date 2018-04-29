class Queen(object):
    def __init__(self, row, column):
        if not 0 <= row <= 7 or not 0 <= column <= 7:
            raise ValueError("Invalid position for queen")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """Whether this queen can attack another."""
        same_row = self.row == another_queen.row
        same_col = self.column == another_queen.column

        if same_row and same_col:
            raise ValueError("Queens can't be at the same position")

        same_diag = abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        return same_row or same_col or same_diag
