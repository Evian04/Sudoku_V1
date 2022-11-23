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

        if not (line or column or square): # If no content was put in argument
            self.content[listFormats[0]] = self.userContentRequest() # Request to the user to manually enter the content of the sudoku in the powerShell
            self.contentUpdate(listFormats[0])
            return

        # else (since the program "return" at the end the if block), set the first non-empty format given as the "reference" to updates the authers
        dictFormat = {
            listFormats[0]: line,
            listFormats[1]: column,
            listFormats[2]: square
        }
        
        for format in listFormats:
            self.content[format] = dictFormat[format]
            self.contentUpdate(format)

    def userContentRequest(self) -> list[list[str]]:
        # This fonction request the content of the sudoku to the user
        finalContent = []
        for i in range(9):
            line = list(input(f"line {i + 1}: ")) # For each line of the sudoku, request to the user the content of the line
            if not len(line) == 9: # if there was more or less than 9 chars (the length of a sudoku line)
                print("You must enter 9 characters")
                return self.userContentRequest() # Re-call the fonction
            else:
                for v in line:
                    if not v in ["1", "2", "3", "4", "5", "6", "7", "8", "9", " "]: # If on of the entered chars was not a digit or a space
                        print("Invalid character entered")
                        return self.userContentRequest() # Re-call the fonction
            # Else append the line obtained to the "final content" 
            finalContent.append(line)
        
        return finalContent
    
    def overWriteContent(self, content: list[list], format: str) -> None:
        # This fonction overwrite all the board
        self.content[format] = content
        self.contentUpdate(format) # and update the authers

    def contentUpdate(self, ref: str) -> None:
        # When a certain content format is modified, this fonction updates the auters
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
    
    def getCellValue(self, format: str, id: tuple) -> str:
        return self.content[format][id[0]][id[1]]
    
    def setCellValue(self, digit: str, format: str, id: tuple[int]):
        # This fonction allow you to set the value of a cell
        self.content[format][id[0]][id[1]] = digit
        self.contentUpdate(format)
    
    def removeDigit(self, format: str, id: tuple[int]):
        # This fonction remove the value of the cell with id coordinates
        self.content[format][id[0]][id[1]] = " "
        self.contentUpdate(format)
    
    def isBoardFull(self) -> bool:
        for iPart in range(9):
            for iCell in range(9):
                if self.content[listFormats[0]][iPart][iCell] == " ":
                    return False
        
        return True

    def check(self) -> Bundle:
        # This fonction return if there are errors ? and if yes, where ?
        # by using the class "Bundle"
        isConflicts = False
        formatsConflicts = []
        idConflicts = []
        doubloonDigitConflicts = []
        
        for format in listFormats:
            for iPart in range(9):
                listDigits = []
                for iCell in range(9):
                    caseValue = self.getCaseValue(format, (iPart, iCell))
                    if not caseValue == " ":
                        if caseValue in listDigits:
                            isConflicts = True
                            formatsConflicts.append(format)
                            idConflicts.append((iPart, iCell))
                            doubloonDigitConflicts.append(caseValue)
                        listDigits.append(caseValue)
        
        return Bundle(isConflicts, formatsConflicts, idConflicts, doubloonDigitConflicts)
    
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
