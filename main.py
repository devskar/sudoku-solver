from sudoku import *

example_sudokus = ['000260701680070090190004500820100040004602900050003028009300074040050036703018000',
                   '000690400029005003001034008980001070207069031003207540830900007005020000106573004',
                   '3002041003204001',
                   '0000041003204001']

inp = input('insert sudoku: ')

# creating sudoku object
sudoku = Sudoku(int(math.sqrt(len(inp))))

# filling cells list
for i in range(len(inp)):
    cell = Cell(int(inp[i]), sudoku)

    sudoku.cellslist[i % sudoku.length][int(i // sudoku.length)] = cell

    cell.update()

while True:
    i = sudoku.solve()

    print(i)

    if i == 0:
        break

sudoku.print()
