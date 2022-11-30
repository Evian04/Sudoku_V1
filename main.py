from src.module.grid import Grid
from src.module.cell import Cell
from src.module.utils import read_file
import time


path = input("Enter the absuolute path of your sudoku (make sure that there is `/` and not `\\` as file separator)\n-> ")
content = read_file(path)
sdk = Grid(content)
start_time = time.time()
is_process_displayed = False # `False` to not display the process

if sdk.solve(is_process_displayed):
    if not is_process_displayed:
        sdk.print_grid(False)
    
    print(f"\nTime taken : {time.time() - start_time} seconds")

else: quit("Cannot solve sudoku.")