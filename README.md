# SudokuSolver

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Interactive Sudoku Grid](#interactive-sudoku-grid)
  - [Backtracking Algorithm](#backtracking-algorithm)
  - [Error Checking](#error-checking)
  - [Theme Toggle](#theme-toggle)
  - [Erase Mode](#erase-mode)
  - [Puzzle Reset](#puzzle-reset)
  - [Solve Button](#solve-button)
  - [Responsive Layout](#responsive-layout)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [User Interactions](#user-interactions)
- [Code Structure](#code-structure)
  - [main.py](#mainpy)
  - [windows/sudoku_solver_window.py](#windowsudoku_solver_windowpy)
  - [helpers/sudoku_solver.py](#helperssudoku_solverpy)
  - [widgets/theme_toggle.py](#widgetstheme_togglepy)
  - [resources/styles.py](#resourcesstylespy)
- [How it Works](#how-it-works)
  - [Sudoku Grid](#sudoku-grid)
  - [The Solver Algorithm](#the-solver-algorithm)
  - [Theme Toggle](#theme-toggle-1)
  - [User Interaction](#user-interaction)
  - [Error Handling](#error-handling)
- [Example](#example)
- [License](#license)

## Overview

The **SudokuSolver** application is designed to provide a simple yet effective solution to Sudoku puzzles. With a focus on both functionality and usability, it features an intuitive graphical interface using PyQt6. Users can manually input Sudoku puzzles, interact with the grid, and solve them automatically with a single click. The backtracking algorithm attempts to fill in the grid step-by-step, trying different possibilities until it finds the correct solution. The application also provides real-time feedback on invalid inputs and offers both light and dark themes for a customizable user experience.

## Features

### Interactive Sudoku Grid

The application provides a 9x9 Sudoku grid, where each cell can be filled with a number from 1 to 9. This grid serves as the interactive interface for users to input their Sudoku puzzle manually. Each cell in the grid is represented by a button, and the number input is displayed within the button itself. The user clicks on a button to select a cell and can then input a number using the number buttons or erase their input with the "Erase" button. The grid's layout is designed to be clear and easy to use, with a uniform structure and visual indicators for valid or invalid inputs.

### Backtracking Algorithm

The heart of the **SudokuSolver** application is the backtracking algorithm, which is used to solve the Sudoku puzzle. The algorithm works by trying to place numbers in empty cells and checking whether the current configuration adheres to Sudoku rules (i.e., no repeating numbers in rows, columns, or 3x3 subgrids). If a number cannot be placed in a cell due to conflicts, the algorithm backtracks and tries another number, continuing this process until the puzzle is solved or determined to be unsolvable. This technique is efficient and guarantees a solution if the puzzle is valid.

### Error Checking

The application includes error checking functionality to ensure the puzzle is valid before solving. If the user enters an invalid number (such as two identical numbers in a row or column), the cell will be highlighted to indicate the error. This provides real-time feedback to the user, allowing them to correct mistakes before attempting to solve the puzzle. Additionally, when the puzzle is solved, any invalid configurations are flagged, and an error message is displayed, ensuring users understand why the puzzle cannot be solved.

### Theme Toggle

**SudokuSolver** supports both light and dark themes, which can be toggled by the user through a simple button click. The theme toggle feature allows the user to switch between themes for a more comfortable visual experience. The dark theme uses dark background colors with lighter text, while the light theme features a traditional light background with dark text. The theme settings are saved and applied automatically when the application is reopened.

### Erase Mode

The "Erase" mode enables users to remove any numbers they have entered in the puzzle grid. Clicking the "Erase" button allows the user to erase incorrect inputs, clearing the selected cell for a new number. This feature helps users correct mistakes or reset individual cells without resetting the entire puzzle.

### Puzzle Reset

The "Reset" button allows users to clear the entire puzzle and start over. This is useful when the user wants to begin with a new puzzle or test different configurations. The reset button clears all inputs in the grid, returning it to its initial empty state.

### Solve Button

The "Solve" button automatically solves the entire puzzle using the backtracking algorithm. Once clicked, the application will attempt to fill in all the empty cells, solving the puzzle step-by-step. If the puzzle is solvable, the solution will be displayed in the grid. If the puzzle is invalid or unsolvable, the application will display an error message indicating the issue.

### Responsive Layout

The application has a responsive layout that adjusts based on the window size. Whether the window is maximized or resized, the grid and UI components maintain their proportions, ensuring a consistent user experience on different screen sizes. This flexibility makes the application accessible on both small and large screens, such as laptops and desktops.

## Technologies

- **Python 3.x**: The primary programming language used to develop the application.
- **PyQt6**: A Python binding for the Qt6 framework, which is used for the graphical user interface. PyQt6 provides all the necessary components to create windows, buttons, and grids for the application.
- **Backtracking Algorithm**: The algorithm used to solve the Sudoku puzzle. It attempts to fill empty cells with numbers and backtracks when it encounters an invalid configuration.
- **CSS Stylesheets**: The application's UI elements are styled using CSS, which allows for easy customization of the appearance, including the light and dark themes.

## Installation

To get started with the **SudokuSolver** application, follow these installation steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/eldrionix/SudokuSolver.git
   cd SudokuSolver
   ```

2. **Set up a virtual environment (optional but recommended):**

    This ensures that the application runs with the correct dependencies without affecting your global Python installation.
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    Install the necessary Python packages listed in requirements.txt.
    ```bash
    pip install -r requirements.txt
    ```

4. **Install PyQt6:**

    If you haven't installed PyQt6 yet, you can do so by running:
    ```bash
    pip install PyQt6
    ```

## Usage

### Starting the Application

To run the application, use the following command in the terminal:
```bash
python main.py
```
This will launch the main window of the SudokuSolver application. You will see a 9x9 grid where you can enter numbers, and several buttons to interact with the puzzle (Solve, Erase, Reset, Theme Toggle).

### User Interactions

- **Input numbers:** Click on a grid cell to select it, then choose a number between 1 and 9 using the number buttons at the bottom of the window.
- **Erase numbers:** Use the "Erase" button to remove any number you entered.
- **Solve the puzzle:** Click the "Solve" button to automatically solve the puzzle using the backtracking algorithm.
- **Reset the puzzle:** Click the "Reset" button to clear the grid and start over.
- **Switch themes:** Use the "Theme Toggle" button to switch between light and dark themes.

## Code Structure

The application follows a modular design with separate files for the main application logic, window UI, helper functions, and widgets.
```bash
SudokuSolver/
├── main.py                     # Entry point for the application
├── windows/
│   └── sudoku_solver_window.py  # Main window containing the Sudoku grid and UI components
├── helpers/
│   └── sudoku_solver.py        # Backtracking algorithm used to solve the Sudoku puzzle
├── widgets/
│   └── theme_toggle.py         # Widget for toggling between light and dark themes
├── resources/
│   └── styles.py               # Custom styles for the application, including themes
└── requirements.txt            # List of dependencies for the application
```

### main.py

This file is the entry point of the application. It initializes the PyQt6 application and sets up the main window (SudokuSolverWindow). The window contains the grid and all necessary UI components for interacting with the puzzle.

### windows/sudoku_solver_window.py

This file defines the main window (SudokuSolverWindow), which contains the 9x9 grid and buttons for interacting with the Sudoku puzzle. It sets up the layout and connects the buttons to their respective functionality (input, erase, solve, reset, etc.).

### helpers/sudoku_solver.py

This file contains the logic for solving the Sudoku puzzle using the backtracking algorithm. It provides functions for checking the validity of a number placement and for solving the puzzle step-by-step.

### widgets/theme_toggle.py

This file defines the ThemeToggle widget, which is responsible for switching between light and dark themes. It interacts with the main window to update the application's appearance when the user toggles the theme.

### resources/styles.py

This file contains the custom styles for the application's UI elements. It includes CSS rules for both the light and dark themes, as well as any other visual customizations for buttons, grid cells, and text.

## How it Works

### Sudoku Grid

The 9x9 grid is composed of buttons that represent each cell in the Sudoku puzzle. When a user clicks on a button, they can input a number or erase it. The grid is dynamically generated in the SudokuSolverWindow class, and each button is connected to event handlers that process user inputs.

### The Solver Algorithm

The backtracking algorithm is implemented in the SudokuSolver helper class. It attempts to fill empty cells with valid numbers while checking for conflicts in rows, columns, and subgrids. When a number cannot be placed, the algorithm backtracks and tries a different number.

### Theme Toggle

The theme toggle functionality is managed through the ThemeToggle widget. When the user clicks the "Theme Toggle" button, it changes the application’s CSS styles by switching between predefined light and dark themes.

### User Interaction

Users interact with the application by selecting cells, entering numbers, and using the buttons to erase, reset, or solve the puzzle. The solver runs step-by-step to find the solution, and users can view the progress in real-time.

### Error Handling

Error checking is performed when the user enters invalid numbers. If a conflict is detected, the application will highlight the affected cells and prevent the user from continuing until the error is resolved. The solver also includes error handling to manage unsolvable puzzles.

## Example

![Example](assets/example.gif)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
