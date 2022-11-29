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
        
        if display:
            os.system("cls")
            self.print_grid()
        
        fec = self.first_empty_cell() # first empty cell
        ld = self.get_possible_digits(fec) # list digits

        if len(ld) == 0:
            return False
        
        for d in ld:
            self.set(fec, d)
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
    
    # def print_grid(self):
    #     grid = self.get_as()
    #     string_to_print = ""

    #     for line in grid:
    #         sub_string = ""
    #         for cell in line:
    #             sub_string += cell + " "
    #             if line.index(cell) in [2, 5]:
    #                 sub_string += "| "
            
    #         string_to_print += sub_string + "\n"

    #         if grid.index(line) in [2, 5]:
    #             string_to_print += "-" * 6 + "+" + "-" * 7 + "+" + "-" * 6 + "\n"
        
    #     print("\n" + string_to_print)
    def print_grid(self):
        content = self.get_as()
        template = """
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}
        ------+-------+------
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}
        ------+-------+------
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}
        {} {} {} | {} {} {} | {} {} {}"""
         
        print(template.format(
            content[0][0], content[0][1], content[0][2], content[0][3], content[0][4], content[0][5], content[0][6], content[0][7], content[0][8],
            content[1][0], content[1][1], content[1][2], content[1][3], content[1][4], content[1][5], content[1][6], content[1][7], content[1][8],
            content[2][0], content[2][1], content[2][2], content[2][3], content[2][4], content[2][5], content[2][6],content[2][7], content[2][8],
            content[3][0], content[3][1], content[3][2], content[3][3], content[3][4], content[3][5], content[3][6], content[3][7], content[3][8],
            content[4][0], content[4][1], content[4][2], content[4][3], content[4][4], content[4][5], content[4][6], content[4][7], content[4][8],
            content[5][0], content[5][1], content[5][2], content[5][3], content[5][4], content[5][5], content[5][6], content[5][7], content[5][8],
            content[6][0], content[6][1], content[6][2], content[6][3], content[6][4], content[6][5], content[6][6], content[6][7], content[6][8],
            content[7][0], content[7][1], content[7][2], content[7][3], content[7][4], content[7][5], content[7][6], content[7][7], content[7][8],
            content[8][0], content[8][1], content[8][2], content[8][3], content[8][4], content[8][5], content[8][6], content[8][7], content[8][8]
        ))