from src.module.cell import Cell


class Sudoku:
    """ Contains the functions that apply directly to the sudoku """
    
    def __init__(self, content: list[list[str]], kind):
        self.content = content
        self.kind = kind
        
    def solve(self): pass

    def set(self, box: Cell, value: str):
        if not value in [str(n + 1) for n in range(9)]: # = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            quit(f"Error function set : invalid value entered : {value}")
        
        self.content[box.get_a()][box.get_b()] = value

    def unset(self, box: Cell):
        self.content[box.get_a()][box.get_b()] = " "

    def is_valid(self): pass

    def first_empty_cell(self) -> Cell:
        """ Return first empty cell """
        
        for index_line in range(len(self.content)):
            for index_cell in range(len(self.content[index_line])):
                if self.content[index_line][index_cell] == " ":
                    return Cell(" ", index_line, index_cell)

    def is_full(self) -> bool:
        for line in self.get_content():
            for num in line:
                if num == " ":
                    return False
        return True
            
        
    def as_column(self): pass
    def as_square(self): pass

    def get_content(self):
        return self.content