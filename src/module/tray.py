from termcolor import colored
from src.module.utils import contentFormatConverter
from src.module.bundle import Bundle
listFormats = ("line", "column", "square")


class Tray:
    """ Allows you to manage the actions performed on the Sudoku grid. """

    def __init__(self, line: list[list[str]] = [], column: list[list[str]] = [], square: list[list[str]] = []):
        self.content = {
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
        return self.content[format][id[0]][id[1]]
    
    def addDigit(self, digit: str, format: str, id: tuple[int]) -> None:
        # This fonction set the value of the case with id coordinates
        self.content[format][id[0]][id[1]] = digit
        self.contentUpdate(format)
    
    def removeDigit(self, format: str, id: tuple[int]) -> None:
        # This fonction remove the value of the case with id coordinates
        self.content[format][id[0]][id[1]] = " "
        self.contentUpdate(format)
    
    def check(self) -> Bundle:
        # This fonction return some information about the tray like if it's full ? if there is errors ? and if yes, where ? using the class "Bundle"
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
        
        return Bundle(isFull,isError, formatsErrors, idErrors, doubloonDigitErrors)
    
    def printBoard(self, color: str = "") -> None:
        # This fonction print the board in the consol
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
