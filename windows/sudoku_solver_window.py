from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QFrame, QSizePolicy, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QCursor
from helpers.sudoku_solver import SudokuSolver
from resources.styles import styles
from widgets.theme_toggle import ThemeToggle


class SudokuSolverWindow(QMainWindow):
    """Main window for the Sudoku Solver application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(750, 550)
        self.current_theme = "light"
        self.setStyleSheet(styles[f"main_window_{self.current_theme}"])

        self.user_inputted = set()
        self.selected_number = None
        self.selected_button = None
        self.eraser_mode = False
        self.solved = False

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QGridLayout(main_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        frame = QFrame()
        frame.setFixedSize(380, 380)
        frame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        frame.setStyleSheet("border: 7px solid #C8C8C8; color: #000; background-color: #D3D3D3")
        
        theme_toggle = ThemeToggle(parent_window=self, initial_theme=self.current_theme)
        main_layout.addWidget(theme_toggle, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        sudoku_grid_layout = QGridLayout(frame)
        sudoku_grid_layout.setContentsMargins(0, 0, 0, 0)
        sudoku_grid_layout.setSpacing(0)

        self.sudoku_buttons = {}

        for row in range(9):
            for col in range(9):
                button = QPushButton()
                button.setFixedSize(42, 42)
                button.setFont(QFont("Inter", 25))
                button.setStyleSheet(styles["sudoku_button"])
                button.clicked.connect(lambda _, r=row, c=col: self.on_sudoku_button_click(r, c))  # Event binding
                self.sudoku_buttons[(row, col)] = button
                sudoku_grid_layout.addWidget(button, row, col)

        main_layout.addWidget(frame, 1, 0)

        self.number_buttons_frame = QFrame()
        self.number_buttons_frame.setFixedSize(200, 200)
        self.number_buttons_frame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.number_buttons_frame.setStyleSheet("background-color: #D3D3D3; border: 7px solid #C8C8C8")

        number_buttons_layout = QGridLayout(self.number_buttons_frame)
        number_buttons_layout.setContentsMargins(0, 0, 0, 0)
        number_buttons_layout.setSpacing(0)

        numbers = [str(i) for i in range(1, 10)]
        for idx, number in enumerate(numbers):
            button = QPushButton(number)
            button.setFixedSize(63, 63)
            button.setFont(QFont("Inter", 35))
            button.setStyleSheet(styles["number_button"])
            button.clicked.connect(lambda _, num=number, btn=button: self.on_number_button_click(num, btn))  # Event binding
            row = idx // 3
            col = idx % 3
            number_buttons_layout.addWidget(button, row, col)

        main_layout.addWidget(self.number_buttons_frame, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        buttons_layout = QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.eraser_button = QPushButton("Eraser")
        self.eraser_button.setFixedSize(197, 60)
        self.eraser_button.setFont(QFont("Inter", 25))
        self.eraser_button.setStyleSheet(styles["eraser_button"])
        self.eraser_button.clicked.connect(self.on_eraser_button_click)
        buttons_layout.addWidget(self.eraser_button)

        buttons_layout.addSpacing(10)

        solve_button = QPushButton("Solve")
        solve_button.setFixedSize(197, 50)
        solve_button.setFont(QFont("Inter", 25))
        solve_button.setStyleSheet(styles["solve_button"])
        solve_button.clicked.connect(self.on_solve_button_click)
        buttons_layout.addWidget(solve_button)

        reset_button = QPushButton("Reset")
        reset_button.setFixedSize(197, 50)
        reset_button.setFont(QFont("Inter", 25))
        reset_button.setStyleSheet(styles["reset_button"])
        reset_button.clicked.connect(self.on_reset_button_click)
        buttons_layout.addWidget(reset_button)

        quit_button = QPushButton("Quit")
        quit_button.setFixedSize(197, 50)
        quit_button.setFont(QFont("Inter", 25))
        quit_button.setStyleSheet(styles["quit_button"])
        quit_button.clicked.connect(self.close)
        buttons_layout.addWidget(quit_button)

        right_side_layout = QVBoxLayout()
        right_side_layout.addWidget(self.number_buttons_frame)
        right_side_layout.addLayout(buttons_layout)

        main_layout.addLayout(right_side_layout, 1, 1)

    def on_number_button_click(self, number: str, btn: QPushButton):
        """Handle the click event for number buttons."""
        if self.eraser_mode:
            self.eraser_mode = False
            self.eraser_button.setStyleSheet(styles["eraser_button"])
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.selected_number = number
        self.highlight_selected_number_button(btn)

    def on_sudoku_button_click(self, row: int, col: int):
        """Handle the click event for Sudoku grid buttons."""
        if self.solved:
            return
        button = self.sudoku_buttons[(row, col)]
        if self.eraser_mode:
            button.setText("")
            self.user_inputted.discard((row, col))
            button.setStyleSheet(styles["user_input_cell"])
        elif self.selected_number:
            button.setText(self.selected_number)
            self.user_inputted.add((row, col))
            button.setStyleSheet(styles["user_input_cell"])

    def on_eraser_button_click(self):
        """Handle the click event for the eraser button."""
        self.selected_number = None
        self.eraser_mode = True
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))

    def highlight_selected_number_button(self, selected_button: QPushButton):
        """Highlight the selected number button."""
        if self.selected_button:
            self.selected_button.setStyleSheet(styles["number_button"])

        selected_button.setStyleSheet(styles["selected_number_button"])
        self.selected_button = selected_button

    def on_reset_button_click(self):
        """Handle the click event for the reset button."""
        self.user_inputted = set()
        self.solved = False
        for button in self.sudoku_buttons.values():
            button.setText("")
            button.setStyleSheet(styles["user_input_cell"])
            button.setEnabled(True)

    def highlight_invalid_cells(self, positions):
        """Highlight invalid cells in the Sudoku grid."""
        for pos in positions:
            row, col = pos
            button = self.sudoku_buttons[(row, col)]
            button.setStyleSheet(styles["invalid_cell"])

    def on_solve_button_click(self):
        """Handle the click event for the solve button."""
        try:
            board = [
                [int(self.sudoku_buttons[(row, col)].text()) if self.sudoku_buttons[(row, col)].text() else 0
                 for col in range(9)]
                for row in range(9)
            ]
            solver = SudokuSolver(board)

            is_valid, invalid_positions = solver.is_board_valid()

            if not is_valid:
                self.highlight_invalid_cells(invalid_positions)
                self.show_error_dialog("An error occurred!", "The current Sudoku configuration is invalid.")
                return

            if solver.solve():
                self.solved = True
                for row in range(9):
                    for col in range(9):
                        button = self.sudoku_buttons[(row, col)]
                        button.setText(str(solver.board[row][col]))
                        if (row, col) in self.user_inputted:
                            button.setStyleSheet(styles["user_input_cell"])
                        else:
                            button.setStyleSheet(styles["auto_filled_cell"])
                        button.setEnabled(False)
            else:
                self.show_error_dialog("An error occurred!", "The Sudoku puzzle cannot be solved.")

        except ValueError:
            self.show_error_dialog("Invalid Input", "Only numbers from 1 to 9 are allowed.")

    def show_error_dialog(self, title: str, message: str):
        """Show an error dialog with the specified title and message."""
        QMessageBox.critical(self, title, message)

    def switch_theme(self, theme: str):
        """Switch the theme between light and dark."""
        self.current_theme = theme

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(250)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.animation.finished.connect(self.apply_theme)

        self.animation.start()
        
    def apply_theme(self):
        """Apply the new theme and restore full opacity."""
        self.setStyleSheet(styles[f"main_window_{self.current_theme}"])

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(250)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.start()
        
