from src.module.sudoku import Sudoku


class Cell:
    """ Groups the important data for a square """
    
    def __init__(self, value, a, b):
        self.value = value
        self.a = a
        self.b = b
    
    def possible_digit(self, sdk: Sudoku): pass
    
    def get_value(self):
        return self.value
    
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y