from .utils import get_index_as
from .cell import Cell


class Grid:
    """ Contains the functions that apply directly to the Grid """
    
    def __init__(self, content: list[list[str]]):
        self.content = content
        
    def solve(self):
        """ Solve this fucking Sudoku """

    def set(self, cell: Cell, value: str):
        """ Set the value of the given cell to `value` """
        
        if not value in [str(n + 1) for n in range(9)]:
            quit(f"The value '{value}' must be between 0 and 9 includes.")
        self.content[cell.get_a()][cell.get_b()] = value

    def unset(self, cell: Cell):
        """ Restores the value of the given cell to ' ' """
        
        self.content[cell.get_a()][cell.get_b()] = " "

    def is_valid(self) -> bool:
        """ Checks by row, by column and by group of cells if the sudoku is valid """

        # verification in line format
        for f in ["line", "column", "square"]:
            for group in self.get_as(f):
                for num in group:
                    if num not in group[0:group.index(num)] + group[group.index(num)+1:-1] or num == " ":
                        continue
                    else:
                        print(f"The number '{num}' at the {f} {self.get_as(f).index(group)} and the {group.index(num)+1} character is already present in the {f}.")
                        return False
        return True
                

    def first_empty_cell(self) -> Cell:
        """ Return the first empty cell """
        
        for i_line in range(9):
            for i_num in range(9):
                if self.get_as("line")[i_line][i_num] == " ":
                    return Cell(
                        self.get_as()[i_line][i_num],
                        i_line,
                        i_num
                    )

    def is_full(self) -> bool:
        """ Check if Grid is full """
        
        for line in self.get_as():
            for num in line:
                if num == " ":
                    return False
        return True
    
    def get_as(self, kind: str = "line") -> list[list[str]]:
        """
        Takes a grid in linear format and pulls out another one of `kind` type.
        Returns by default the current grid in linear format.
        """
        
        # create a list of list of empty string, that's the future content to return
        new_content = [["" for b in range(9)] for a in range(9)]
        
        for i_line in range(9):
            for i_num in range(9):
                index_converted = get_index_as(i_line, i_num, kind)
                new_content[index_converted.get_a()][index_converted.get_b()] = self.content[i_line][i_num]
        return new_content
