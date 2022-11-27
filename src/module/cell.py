class Cell:
    """ Groups the important data for a square """
    
    def __init__(self, value: str or None, a: int, b: int):
        self.value = value
        self.a = a
        self.b = b
    
    def get_possible_digits(self, grid) -> list[str]:
        """
        Allows to collect all the possible numbers
        for a cell based on its row, column and cell group.
        """
        
        if grid[self.get_a()][self.get_b()] != " ":
            return [grid[self.get_a()][self.get_b()]]

        list_digits = [str(a + 1) for a in range(9)]

        for kind in ["line", "column", "square"]:
            for d in grid.get_as(kind)[0]:
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
