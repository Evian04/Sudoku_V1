def read_file(file: str) -> list[list[str]]:
    """ Returns the content of a file as a list of lines containing the characters of the line. """
    
    f = open(file, "r")
    lines = f.read().split("\n")
    f.close()
    sudoku = []
    
    # transform sudoku into a list[list[str]] (sudoku -> lines -> chars)
    for line in lines:
        sudoku.append(list(char for char in line))
    
    # verify that the sudoku is correct
    if len(sudoku) == 9:
        for line in sudoku:
            if len(line) == 9:
                return sudoku
            else: quit("A line must contain a total of 9 chars.")            
    else: quit("The file must contain a total of 9 lines.")