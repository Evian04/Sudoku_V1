def calculatesCoordinates(formats, i: int, i2: int, i3: int) -> tuple:
    # This fonction just return which coordinates the contentFormatConverter has to use according to the formats.
    if formats == "sl" or "ls":
        return (i2 + (i // 3) * 3, i3 + (i % 3) * 3)
    
    elif formats == "lc" or formats == "cl":
        return (i2 * 3 + i3, i)
    
    elif formats == "sc":
        return (i2 * 3 + i // 3, i3 * 3 + i % 3)
    
    elif formats == "cs":
        return (i3 % 3 + (i % 3) * 3, i2 + (i // 3) * 3)
    
    else:
        print("Error Fonction calculatesCoordinates : incompatible formats")
        return ()

def contentFormatConverter(content: list[list], formats: str) -> list[list]:
    # This fonction convert the format of the sudoku infos, like square into line, or line into column.
    toReturn: list = []
    for i in range(9):
        tmpList: list = []
        for i2 in range(3):
            for i3 in range(3):
                print(formats, i, i2, i3)
                tmpList.append(content[calculatesCoordinates(formats, i, i2, i3)[0]][calculatesCoordinates(formats, i, i2, i3)[1]])
        
        toReturn.append(tmpList)
    return toReturn

def printSudokuError(report, game) -> None:
    game.board.printBoard("red")
    for i in range(len(report.formatsErrors)):
        print(f"\nError {i + 1}: Format = {report.formatsErrors[i]}\n         Index = {report.idErrors[i]}\n         Doubloon = {report.doubloonDigitErrors[i]}")

def openFile(src: str) -> list[list[str]]:
    file = open(src, "rt")
    sudoku = file.read()
    file.close()
    sudoku = list(sudoku.split("\n"))

    if len(sudoku) != 9:
        print(f"Error fonction openFile : incompatible format at file {src}")
        return []
    else:
        for line in sudoku:
            if len(line) != 9:
                print(f"Error fonction openFile : incompatible format at file {src}")
                return []
    
    return sudoku