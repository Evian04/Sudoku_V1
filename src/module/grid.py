from .utils import get_index_as
from .cell import Cell
import os


class Grid:
    """ Contains the functions that apply directly to the Grid """
    
    def __init__(self, content: list[list[str]]):
        self.content = content
        
    def solve(self, display: bool) -> bool:
        """ Solve this fucking Sudoku """
        if self.is_full():
            return self.is_valid()
        
        fec = self.first_empty_cell() # first empty cell
        ld = self.get_possible_digits(fec) # list digits

        if len(ld) == 0:
            return False
        
        for d in ld:
            self.set(fec, d)

            if display:
                self.print_grid(True)

            if self.solve(display):
                return True
        
        self.unset(fec)
        return False

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
                    # if num not in group[0:group.index(num)] + group[group.index(num)+1:-1] or num == " ":
                    if not group.count(num) > 1 or num == " ": continue
                    else:
                        print(f"'{num}' at the {f} {self.get_as(f).index(group)} and the {group.index(num)+1} character is already present in the {f}.")
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

    def get_possible_digits(self, cell: Cell) -> list[str]:
        """
        Allows to collect all the possible numbers
        for a cell based on its row, column and cell group.
        """
        
        if cell.get_value() != " ":
            return [cell.get_value()]

        list_digits = [str(a + 1) for a in range(9)]

        for kind in ["line", "column", "square"]:
            for d in self.get_as(kind)[get_index_as(cell.get_a(), cell.get_b(), kind).get_a()]:
                if d != " ":
                    if d in list_digits:
                        list_digits.remove(d)
        return list_digits
    
    def print_grid(self, clear_term: bool):
        grid = self.get_as()
        string_to_print = ""

        for index_line in range(len(grid)):
            sub_string = ""
            for index_cell in range(len(grid[index_line])):
                sub_string += grid[index_line][index_cell] + " "
                if index_cell in [2, 5]:
                    sub_string += "| "
            
            string_to_print += sub_string + "\n"

            if index_line in [2, 5]:
                string_to_print += "-" * 6 + "+" + "-" * 7 + "+" + "-" * 6 + "\n"
        
        if clear_term:
            os.system("cls")

        print("\n" + string_to_print)