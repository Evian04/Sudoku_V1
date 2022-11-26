from src.module.utils import read_file
from src.module.sudoku import Sudoku
from src.module.cell import Cell


sudoku_as_line = read_file("model.txt")

sudoku = Sudoku(sudoku_as_line)
fec = sudoku.first_empty_cell()
print(fec)