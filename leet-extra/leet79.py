class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)  # row.
        m = len(board[0])  # col.
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        for i in range(n):
            for j in range(m):
                visited = {(i,j)}
                if self.helper(board, word, directions, (i,j), n, m, visited, 0):
                    return True

        return False


    def helper(self, board, word, directions, start, n, m, visited, word_index):
        if board[start[0]][start[1]] == word[word_index]:
            if word_index == len(word) - 1:
                return True

            for x1, y1 in directions:
                x = start[0] + x1
                y = start[1] + y1
                if 0 <= x < n \
                    and 0 <= y < m \
                    and (x,y) not in visited:
                    # Make the move.
                    visited.add((x,y))
                    # Move on to the next character in word.
                    if self.helper(board, word, directions, (x,y), n, m, visited, word_index+1):
                        return True
                    # Backtrack.
                    visited.remove((x,y))

        return False