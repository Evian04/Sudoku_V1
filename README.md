This project aims to solve a sudoku grid using a backtracking function (`src/module/grid.solve()`)
To solve the sudoku, you must enter the grid line per line in the model.txt file,
each line of this file represent a line of the sudoku, and must contain 9 characters, the corresponding digit or a space if the cell is empty (make sure that there is 9 character in each lines even if the last chars are spaces)
Then, save the file `model.txt`, and run the `main.py` python script.
The solved sudoku will be print as 9 lists of 9 chars. The scirpt will also verify the final grid and print the boolean answer (True / False) so make sure that `True` is print. Finally, the scrpit will print the time it took to solve the grid in seconds.
If `Cannot solve the sudoku` appears, it means that the program didn't find any solution, and that there is an error in the given grid so verify what you written in the `model.txt` file.