from src.module.square import Square


class Sudoku:
    """ Contains the functions that apply directly to the sudoku """
    
    def __init__(self, content: list[list[str]], kind):
        self.content = content
        self.content = kind
        
    def solve(self): pass
    def set(self, sqr: Square, value): pass
    def unset(self, sqr: Square): pass
    def is_valid(self): pass
    def first_empty_square(self): pass
    def game_over(self): pass
    def as_column(self): pass
    def as_square(self): pass