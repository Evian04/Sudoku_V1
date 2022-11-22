from src.module.utils import contentFormatConverter
from src.module.tray import Tray
listFormats = ("line", "column", "square")


class Solver:
    """ Gathers the conclusive functions that allow to solve the sudoku. """

    def __init__(self, line: list[list[str]] = [], column: list[list[str]] = [], square: list[list[str]] = []) -> None:
        self.board = Tray(line = line, column = column, square = square)
        self.possibleDigit: dict[str: list[list[dict[str: bool or int]]]] = {
            format: [[{
                "1": True,
                "2": True,
                "3": True,
                "4": True,
                "5": True,
                "6": True,
                "7": True,
                "8": True,
                "9": True,
                "total": 9
                    } for a in range(9)
                ] for b in range(9)
            ] for format in listFormats
        }
    
    def updatePossibleDigit(self, ref: str) -> None:
        # This fonction update the authers content's formats when one is modify
        for iPart in range(9):
            for iCase in range(9):
                total = 0
                for iDigit in range(9):
                    total += self.possibleDigit[ref][iPart][iCase][str(iDigit + 1)]
                self.possibleDigit[ref][iPart][iCase]["total"] = total

        if ref == listFormats[0]:
            self.possibleDigit[listFormats[1]] = contentFormatConverter(self.possibleDigit[ref], "lc")
            self.possibleDigitlistFormats[[2]] = contentFormatConverter(self.possibleDigit[ref], "ls")
        
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
            content: list[list[dict[str: bool or int]]] = self.board.content[format]
            for iPart in range(len(content)):
                listDigits: list[str] = []
                for iCase in range(len(content[iPart])):
                    caseValue: str = self.board.getCaseValue(format, (iPart, iCase))
                    if caseValue != " ":
                        listDigits.append(caseValue)
                
                for iCase in range(len(content[iPart])):
                    caseValue = self.board.getCaseValue(format, (iPart, iCase))
                    for digit in listDigits:
                        self.possibleDigit[format][iPart][iCase][digit] = False
            
            self.updatePossibleDigit(format)
    
    def setNewDigit(self) -> None:
        # This fonction set some new digit according to the list of possible digit of each case.
        format = "line"
        for iPart in range(9):
            for iCase in range(9):
                if self.board.getCaseValue(format, iPart, iCase) != " ":
                    continue

                if self.possibleDigit[format][iPart][iCase]["total"] != 1:
                    continue

                for digit in range(9):
                    if self.possibleDigit[format][iPart][iCase][str(digit + 1)]:
                        self.board.addDigit(str(digit + 1), format, (iPart, iCase))
                        continue

        self.updatePossibleDigit(format)