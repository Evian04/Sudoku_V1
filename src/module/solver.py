from src.module.utils import contentFormatConverter
from src.module.tray import Tray
listFormats = ("line", "column", "square")

class Solver:
    """ Gathers the conclusive functions that allow to solve the sudoku. """

    def __init__(self, line: list = [], column: list = [], square: list = []) -> None:
        self.board = Tray(line = line, column = column, square = square)
        # This variable contain the differents possible digit for every cell of the board
        self.possibleDigit: dict= {
            format: [[[
                str(d + 1) for d in range(9)
            ] for a in range(9)
                ] for b in range(9)
            ] for format in listFormats
        }
    
    def updatePossibleDigit(self, ref: str) -> None:
        # When a certain format of the "possible digits" is modified, the authers are updates with this fonction.
        if ref == listFormats[0]:
            self.possibleDigit[listFormats[1]] = contentFormatConverter(self.possibleDigit[ref], "lc")
            self.possibleDigit[listFormats[2]] = contentFormatConverter(self.possibleDigit[ref], "ls")
        
        elif ref == listFormats[1]:
            self.possibleDigit[listFormats[0]] = contentFormatConverter(self.possibleDigit[ref], "cl")
            self.possibleDigit[listFormats[2]] = contentFormatConverter(self.possibleDigit[ref], "cs")
        
        elif ref == listFormats[2]:
            self.possibleDigit[listFormats[0]] = contentFormatConverter(self.possibleDigit[ref], "sl")
            self.possibleDigit[listFormats[1]] = contentFormatConverter(self.possibleDigit[ref], "sc")
        
        else:
            print("Error Fonction contentUpdate : incompatible ref")

    def calculatesPossibleDigit(self) -> None:
        # This fonction reduce the possible digit of each case according to the digit that are already set
        for format in listFormats:
            content = self.board.content[format]
            for iPart in range(len(content)):
                listDigits = []
                for iCase in range(len(content[iPart])):
                    caseValue = self.board.getCaseValue(format, (iPart, iCase))
                    if caseValue != " ":
                        listDigits.append(caseValue)
                # This part of the fonction set a list of all the digit that are present in each part of the board (a "part" is the list of all the cells in a line, a column or a square)
                
                for iCase in range(len(content[iPart])):
                    caseValue = self.board.getCaseValue(format, (iPart, iCase))
                    for digit in listDigits:
                        if digit in self.possibleDigit[format][iPart][iCase]:
                            self.possibleDigit[format][iPart][iCase].remove(digit)
                # And this one remove the digits of the obtained list from the possible digits of every empty cells of the part in question
            
            self.updatePossibleDigit(format)
            # And then, the fonction "updates" the authers formats when its modified one of them

    # This fonction doesn't serve anymore since the future "backtracking" fonction will take care of setting the new digits
    # But it will maybe serve one day, never know...
    """
    def setNewDigit(self) -> None:
        # This fonction set some new digit according to the list of possible digit of each case.
        format = listFormats[0]
        for iPart in range(9):
            for iCase in range(9):
                if self.board.getCaseValue(format, (iPart, iCase)) != " ":
                    continue

                if len(self.possibleDigit[format][iPart][iCase]) != 1:
                    continue

                for digit in range(9):
                    if str(digit + 1) in self.possibleDigit[format][iPart][iCase]:
                        self.board.addDigit(str(digit + 1), format, (iPart, iCase))

        self.updatePossibleDigit(format)
        """