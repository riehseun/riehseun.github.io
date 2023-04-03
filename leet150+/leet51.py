class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = []
        for i in range(n):
            board.append([])
            for _ in range(n):
                board[i].append(".")

        column = set()
        diag = set()
        anti_diag = set()
        result = []
        self.helper(0, n, board, column, diag, anti_diag, result)
        return result

    def helper(self, row, n, board, column, diag, anti_diag, result):
        # If reached the last row, add to the result and return.
        if row == n:
            result.append(["".join(row) for row in board])
            return

        # Try to place a queen in each column.
        for col in range(n):
            if col not in column \
                and row+col not in diag \
                and row-col not in anti_diag:
                # Place the queen.
                board[row][col] = "Q"
                # Mark column, diag, anti_diag as occupied.
                column.add(col)
                diag.add(row+col)
                anti_diag.add(row-col)
                # Move on to the next row.
                self.helper(row+1, n, board, column, diag, anti_diag, result)
                # Backtrack. Unplace the queen. Unmark column, diag, anti_diag.
                board[row][col] = '.'
                column.remove(col)
                diag.remove(row+col)
                anti_diag.remove(row-col)