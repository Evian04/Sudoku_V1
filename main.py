from src.module.grid import Grid
from src.module.utils import read_file
import time


path = input("Enter the absuolute path of your sudoku\n-> ")
content = read_file(path)
sdk = Grid(content)
start_time = time.time()
is_process_displayed = False # `False` to not display the process

if sdk.solve(is_process_displayed):
    if not is_process_displayed:
        sdk.print_grid(False, new_cells_color = "green")
    
    else:
        sdk.print_grid(True, new_cells_color = "green")

    print(f"\nTime taken : {time.time() - start_time} seconds")

else: quit("Cannot solve sudoku.")