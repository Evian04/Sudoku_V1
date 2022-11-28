class Cell:
    """ Groups the important data for a square """
    
    def __init__(self, value: str or None, a: int, b: int):
        self.value = value
        self.a = a
        self.b = b

    def get_value(self): return self.value
    def get_a(self): return self.a
    def get_b(self): return self.b
