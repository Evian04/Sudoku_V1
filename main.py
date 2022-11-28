from src.module.grid import Grid
from src.module.utils import read_file
import time


content = read_file("model.txt")
sdk = Grid(content)
start_time = time.time()

if sdk.solve():
    for line in sdk.get_as():
        print(line)
    print(sdk.is_valid())
    print(f"{time.time() - start_time} seconds.")

else: quit("Cannot solve sudoku.")