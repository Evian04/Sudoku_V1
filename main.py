from src.module.grid import Grid
from src.module.utils import read_file


content = read_file("model.txt")
sdk = Grid(content)

if sdk.solve():
    for line in sdk.get_as():
        print(line)
    print(sdk.is_valid())

else: quit("Cannot solve sudoku.")