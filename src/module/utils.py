def read_file(file: str) -> list[list[str]]:
    """ Returns the content of a file as a list of lines containing the characters of the line. """
    
    f = open(file, "r")
    lines = f.read().split("\n")
    f.close()
    sudoku = []
    
    for line in lines:
        sudoku.append(list(char for char in line))
    return sudoku