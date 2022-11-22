from src.module.solver import Solver
from src.module.bundle import Bundle
from src.module.utils import printSudokuError, openFile


game: Solver = Solver(line = openFile("model.txt"))
isFull: bool = False
advancement: list = []
report = game.board.check()

while not isFull and [game.board.content, game.possibleDigit] != advancement and not report.isError:
    advancement = [game.board.content, game.possibleDigit]
    report: Bundle = game.board.check()
    isFull = report.isFull
    
    game.board.printBoard()
    game.calculatesPossibleDigit()
    game.setNewDigit()

if report.isError:
    game.board.printBoard("red")
    printSudokuError(report, game)

elif report.isFull:
    game.board.printBoard("green")

else:
    print("bloqué :/")