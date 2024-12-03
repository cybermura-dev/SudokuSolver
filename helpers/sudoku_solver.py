class SudokuSolver:
    """Sudoku Solver class to solve the Sudoku puzzle."""

    def __init__(self, board):
        """Initialize the SudokuSolver with the given board."""
        self.board = board

    def solve(self):
        """Solve the Sudoku puzzle using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            if self.is_valid(i, row, col):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        """Find an empty cell in the Sudoku board."""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, num, row, col):
        """Check if placing a number in a cell is valid."""
        for x in range(9):
            if self.board[row][x] == num:
                return False

        for x in range(9):
            if self.board[x][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def is_board_valid(self):
        """Check if the current Sudoku board is valid."""
        invalid_positions = set()

        for row in range(9):
            seen = {}
            for col in range(9):
                num = self.board[row][col]
                if num != 0:
                    if num in seen:
                        invalid_positions.add((row, col))
                        invalid_positions.add((row, seen[num]))
                    else:
                        seen[num] = col

        for col in range(9):
            seen = {}
            for row in range(9):
                num = self.board[row][col]
                if num != 0:
                    if num in seen:
                        invalid_positions.add((row, col))
                        invalid_positions.add((seen[num], col))
                    else:
                        seen[num] = row

        for block_row in range(3):
            for block_col in range(3):
                seen = {}
                for i in range(3):
                    for j in range(3):
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        num = self.board[row][col]
                        if num != 0:
                            if num in seen:
                                invalid_positions.add((row, col))
                                invalid_positions.add(seen[num])
                            else:
                                seen[num] = (row, col)

        return len(invalid_positions) == 0, invalid_positions
