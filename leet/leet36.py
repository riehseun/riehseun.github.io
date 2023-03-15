class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        seen = set()

        # Validate row.
        for row in board:
            for num in row:
                if num.isdigit():
                    if num not in seen:
                        seen.add(num)
                    else:
                        return False
            seen = set()

        # Validate col.
        for j in range(n):
            for i in range(n):
                if board[i][j].isdigit():
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False
            seen = set()

        # Validate square from each top left index.
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                for k in range(0,3):
                    for l in range(0,3):
                        if board[i+k][j+l].isdigit():
                            if board[i+k][j+l] not in seen:
                                seen.add(board[i+k][j+l])
                            else:
                                return False
                seen = set()

        return True