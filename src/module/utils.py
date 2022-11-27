from .cell import Cell


def read_file(file: str) -> list[list[str]]:
    """ Returns the content of a file as a list of lines containing the characters of the line. """
    
    with open(file, "r") as file:
        lines = file.read().split("\n")

    sudoku = []
    
    # transform sudoku into a list[list[str]] (sudoku -> lines -> chars)
    for line in lines:
        print(line)
        sudoku.append(list(char for char in line))

    for line in sudoku:
        print(line)
    
    # verify that the sudoku is correct
    if len(sudoku) == 9:
        for line in sudoku:
            if len(line) == 9:
                return sudoku
            else: quit("A line must contain a total of 9 chars.")            
    else: quit("The file must contain a total of 9 lines.")

def get_index_as(a: int, b: int, kind: str) -> Cell:
    """ Convert a given coordinate format to another `kind` format """
    
    match kind:
        case "line": return Cell(None, a, b)
        case "column": return Cell(None, b, a)
        case "square": return Cell(None, b // 3 + (a // 3) * 3, b % 3 + (a % 3) * 3)
