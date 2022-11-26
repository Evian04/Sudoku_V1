from sudoku import Sudoku
from utils import convert_index


class Cell:
    """ Groups the important data for a square """
    
    def __init__(self, value: str, a: int, b: int):
        self.value = value
        self.a = a
        self.b = b
    
    def get_possible_digits(self, sdk: Sudoku) -> list[str]:
        """
        Allows to collect all the possible numbers
        for a cell based on its row, column and cell group.
        """
        
        if sdk[self.a][self.b] != " ":
            return [sdk[self.a][self.b]]

        list_digits = [str(a + 1) for a in range(9)] # = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for kind in ["line", "column", "square"]:
            for d in sdk.content_as(kind)[0]:
                if d != " ":
                    if d in list_digits:
                        list_digits.remove(d)
        
        return list_digits

    def get_value(self):
        return self.value
    
    def get_a(self):
        return self.a
        
    def get_b(self):
        return self.b