from src.module.grid import Grid
from src.module.cell import Cell
from src.module.utils import read_file
import time


content = read_file("./model.txt")
sdk = Grid(content)
start_time = time.time()

if sdk.solve(True): # `False` to not display the process
    sdk.print_grid()
    print(f"{time.time() - start_time} seconds.")

else: quit("Cannot solve sudoku.")