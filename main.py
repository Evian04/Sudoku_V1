from src.module.grid import Grid
from src.module.utils import read_file
import time


content = read_file("pbss/model.txt")
sdk = Grid(content)
start_time = time.time()

if sdk.solve():
    sdk.print_grid()
    print(sdk.is_valid())
    print(f"{time.time() - start_time} seconds.")

else: quit("Cannot solve sudoku.")