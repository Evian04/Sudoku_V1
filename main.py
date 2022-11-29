from src.module.grid import Grid
from src.module.cell import Cell
from src.module.utils import read_file
import time


content = read_file("./model.txt")
sdk = Grid(content)
start_time = time.time()
display = True # `False` to not display the process

if sdk.solve(display):
    if not display:
        sdk.print_grid()
    print(f"\n [     {time.time() - start_time} seconds     ]")

else: quit("Cannot solve sudoku.")