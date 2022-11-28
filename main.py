from src.module.grid import Grid
from src.module.utils import read_file


content = read_file("pbss/model.txt")
sdk = Grid(content)

if sdk.solve():
    print("Sudoku solved !")
    for line in sdk.get_as():
        print(line)

else:
    print("Cannot solve sudoku")