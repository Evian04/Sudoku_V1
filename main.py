from src.module.solver import Solver
from src.module.bundle import Bundle
from src.module.utils import printSudokuError, openFile


solver = Solver(line = openFile("model.txt"))
isFull = False
advancement = []
report = solver.board.check()

while not isFull and [solver.board.content, solver.possibleDigit] != advancement and not report.isError:
    advancement = [solver.board.content, solver.possibleDigit]
    report: Bundle = solver.board.check()
    isFull = report.isFull
    
    solver.board.printBoard()
    solver.calculatesPossibleDigit()
    solver.setNewDigit()

if report.isError:
    solver.board.printBoard("red")
    printSudokuError(report, solver)

elif report.isFull:
    solver.board.printBoard("green")

else:
    print("bloqué :/")