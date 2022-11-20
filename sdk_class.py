from termcolor import colored
from sdk_fonc import contentFormatConverter
listFormats: tuple = ("line", "column", "square")

"""
package's the format that the fonction check return. This class has no fonction, it's just storing information.
"""
class package:

    def __init__(self, isFull: bool, isError: bool, formatsErrors: list[str] = [], idErrors: list[int] = [], doubloonDigitErrors: list[str] = []) -> None:
        self.isFull: bool = isFull
        self.isError: bool = isError
        self.formatsErrors: list[str] = formatsErrors
        self.idErrors: list[int] = idErrors
        self.doubloonDigitErrors: list[str] = doubloonDigitErrors

        if not (len(formatsErrors) == len(idErrors) and len(idErrors) == len(doubloonDigitErrors)):
            print("Error class package : lists's length aren't equals")

"""
tray is the class that's storing the sudoku infos and that manage them, like add a digit, or remove one.
"""
class tray:

    def __init__(self, line: list[list[str]] = [], column: list[list[str]] = [], square: list[list[str]] = []) -> None:
        self.content: dict[str: list[list[str]]] = {
            listFormats[0]: list[list[str]],
            listFormats[1]: list[list[str]],
            listFormats[2]: list[list[str]]
        }

        if not (line or column or square):
            self.content[listFormats[0]] = self.userContentRequest()
            self.contentUpdate(listFormats[0])
            return

        dictFormat = {
            listFormats[0]: line,
            listFormats[1]: column,
            listFormats[2]: square
        }
        for format in listFormats:
            self.content[format] = dictFormat[format]
            self.contentUpdate(format)

    def userContentRequest(self) -> list[list[str]]:
        # This fonction request some information to the user
        toReturn: list[list[str]] = []
        for i in range(9):
            line = list(input(f"line {i + 1}: "))
            if not len(line) == 9:
                print("You must enter 9 characters")
                return self.userContentRequest()
            else:
                for v in line:
                    if not v in ["1", "2", "3", "4", "5", "6", "7", "8", "9", " "]:
                        print("Invalid character entered")
                        return self.userContentRequest()
            toReturn.append(line)
        
        return toReturn
    
    def overWriteContent(self, content: list[list], format: str) -> None:
        # This fonction overwrite the infos
        self.content[format] = content
        self.contentUpdate(format)

    def contentUpdate(self, ref: str) -> None:
        # This fonction update the auther info's formats when one is modify.
        if ref == listFormats[0]:
            self.content[listFormats[1]] = contentFormatConverter(self.content[ref], "lc")
            self.content[listFormats[2]] = contentFormatConverter(self.content[ref], "ls")
        
        elif ref == listFormats[1]:
            self.content[listFormats[0]] = contentFormatConverter(self.content[ref], "cl")
            self.content[listFormats[2]] = contentFormatConverter(self.content[ref], "cs")
        
        elif ref == listFormats[2]:
            self.content[listFormats[0]] = contentFormatConverter(self.content[ref], "sl")
            self.content[listFormats[1]] = contentFormatConverter(self.content[ref], "sc")
        
        else:
            print("Error Fonction contentUpdate : incompatible ref")
    
    def getCaseValue(self, format: str, id: tuple[int]) -> str:
        # This fonction return the value of a case according to its coordinates in a specific format.
        return self.content[format][id[0]][id[1]]
    
    def addDigit(self, digit: str, format: str, id: tuple[int]) -> None:
        # This fonction set the value of the case with id coordinates
        self.content[format][id[0]][id[1]] = digit
        self.contentUpdate(format)
    
    def removeDigit(self, format: str, id: tuple[int]) -> None:
        # This fonction remove the value of the case with id coordinates
        self.content[format][id[0]][id[1]] = " "
        self.contentUpdate(format)
    
    def check(self) -> package:
        # This fonction return some information about the tray like if it's full ? if there is errors ? and if yes, where ? using the class "package"
        isFull: bool = True
        isError: bool = False
        formatsErrors: list[str] = []
        idErrors: list[int] = []
        doubloonDigitErrors: list[str] = []

        #Test Full#
        for i1 in range(9):
            for i2 in range(9):
                if self.content["line"][i1][i2] == " ":
                    isFull = False
                    break
            if not isFull:
                break
        
        #Test Errors#
        for format in listFormats:
            for i1 in range(9):
                listDigits: list = []
                for i2 in range(9):
                    caseValue = self.getCaseValue(format, (i1, i2))
                    if not caseValue == " ":
                        if caseValue in listDigits:
                            isError = True
                            formatsErrors.append(format)
                            idErrors.append((i1, i2))
                            doubloonDigitErrors.append(caseValue)
                        listDigits.append(caseValue)
        
        return package(isFull,isError, formatsErrors, idErrors, doubloonDigitErrors)
    
    def printBoard(self, color: str = "") -> None:
        toPrint: str = ""
        format = listFormats[0]
        for iLine in range(9):
            line = ""
            for iCase in range(9):
                line += self.getCaseValue(format, (iLine, iCase))

                if iCase in [2, 5]:
                    line += "|"
                else:
                    line += " "
            
            if iLine in [2, 5]:
                line += "\n" + "-"*17

            toPrint += line + "\n"
        
        if not color:
            print(toPrint)
        else:
            print(colored(toPrint, color))

"""
sudoku is the class which calculates the action to do in order to complete the sudoku.
"""
class sudoku:

    def __init__(self, line: list[list[str]] = [], column: list[list[str]] = [], square: list[list[str]] = []) -> None:
        self.board: tray = tray(line = line, column = column, square = square)
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