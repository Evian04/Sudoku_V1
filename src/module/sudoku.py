from src.module.cell import Cell


class Sudoku:
    """ Contains the functions that apply directly to the sudoku """
    
    def __init__(self, content: list[list[str]], kind):
        self.content = content
        self.kind = kind
        
    def solve(self): pass
    def set(self, sqr: Cell, value): pass
    def unset(self, sqr: Cell): pass
    def is_valid(self): pass

    def first_empty_cell(self) -> Cell:
        for line in self.content:
            for cell in line:
                if cell.get_value() == " ":
                    return cell

    def is_full(self): pass
    def as_column(self): pass
    def as_square(self): pass

    def get_content(self):
        return self.content