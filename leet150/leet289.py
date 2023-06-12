class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board_copy = board.copy()
        print(board)
        print(board_copy)

        n = len(board_copy)
        m = len(board_copy[0])

        for i in range(n):
            for j in range(m):
                count = self.get_neighbor_count(board_copy, i, j, n, m)
                if count < 2:
                    board[i][j] = 0
                if count == 3:
                    board[i][j] = 1
                if count > 3:
                    board[i][j] = 0

        return board

    def get_neighbor_count(self, board_copy, i, j, n, m):

        count = 0
        print(str(i) +":"+ str(j))
            
        for dir in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
            n_i = i + dir[0]
            n_j = j + dir[1]

            if 0 <= n_i <= n and 0 <= n_j <= m:
                if board_copy[n_i][n_j] == 1:
                    count += 1
            print(count)

        return count
        
