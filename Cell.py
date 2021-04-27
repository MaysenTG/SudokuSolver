# Cell 2021
# This class models a cell in a sudoku, consisting of row, column coordinates and a value. 
# row and column parameters are integers between 1..9,
# values are integers between 0 .. 9, with 0 indicating that the value is still unknown.

class cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col

    def setCol(self, col):
        self.col = col

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def clone(self):
        return cell(self.row, self.col, self.val)
