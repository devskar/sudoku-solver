import math


class Sudoku:

    def __init__(self, length):
        self.length = length
        self.numbers = [*range(1, int(self.length) + 1)]

        self.cellslist = []
        self.setup()

    def setup(self):

        self.cellslist = [[None] * self.length for _ in range(self.length)]

    def solve(self):

        changes = 0

        # checking in x- and y-direction
        for y in range(self.length):
            for x in range(self.length):
                if self.cellslist[x][y].solved:

                    number = self.cellslist[x][y].number

                    for x2 in range(self.length):
                        changes += self.cellslist[x2][y].remove_possibility(number)
                    for y2 in range(self.length):
                        changes += self.cellslist[x][y2].remove_possibility(number)

                    conx = x // math.sqrt(self.length)
                    cony = y // math.sqrt(self.length)

                    x1 = int(conx * math.sqrt(self.length))
                    y1 = int(cony * math.sqrt(self.length))

                    zellen = []

                    for m in range(int(math.sqrt(self.length))):
                        for n in range(int(math.sqrt(self.length))):
                            zellen.append(self.cellslist[x1 + m][y1 + n])

                    for cell in zellen:
                        if number in cell.possibilities:
                            changes += cell.remove_possibility(number)
        return changes

    def print(self):
        for y in range(self.length):
            if y % math.sqrt(self.length) == 0 and y != 0:
                print(['_'] * (self.length + 2))
            row = []

            for x in range(self.length):
                if x % math.sqrt(self.length) == 0 and x != 0:
                    row.append('|')
                row.append(str(self.cellslist[x][y].number))

            print(row)


class Cell:

    def __init__(self, number, sudoku):
        self.number = number
        self.solved = False
        self.sudoku = sudoku
        self.possibilities = sudoku.numbers.copy()

    def remove_possibility(self, number):
        if number in self.possibilities:
            self.possibilities.remove(number)
            self.update()
            return 1
        return 0

    def update(self):

        if len(self.possibilities) == 1:
            self.number = self.possibilities[0]

        if self.number != 0:
            self.solved = True
            self.possibilities.clear()
