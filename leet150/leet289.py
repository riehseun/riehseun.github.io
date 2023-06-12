class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Denote new 0 as -1 and new 1 as 2.

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):

                count = 0

                for dir in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
                    n_i = i + dir[0]
                    n_j = j + dir[1]

                    if 0 <= n_i < n and 0 <= n_j < m and abs(board[n_i][n_j]) == 1:
                            count += 1

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1
                else:
                    if count == 3:
                        board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

        return board