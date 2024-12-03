import sys
from PyQt6.QtWidgets import QApplication
from windows.sudoku_solver_window import SudokuSolverWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuSolverWindow()
    window.show()
    sys.exit(app.exec())