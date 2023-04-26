from collections import defaultdict

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        graph = defaultdict(list)
        all_o = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if i != 0 and board[i-1][j] == "O":
                        graph[(i,j)].append((i-1,j))
                    if i != len(board)-1 and board[i+1][j] == "O":
                        graph[(i,j)].append((i+1,j))
                    if j != 0 and board[i][j-1] == "O":
                        graph[(i,j)].append((i,j-1))
                    if j != len(board[0])-1 and board[i][j+1] == "O":
                        graph[(i,j)].append((i,j+1))
                    all_o.add((i,j))

        explored_so_far = set()
        for i, j in all_o:
            if i != 0 \
                and i != len(board)-1 \
                and j != 0 \
                and j != len(board[0])-1 \
                and board[i-1][j] == "X" \
                and board[i+1][j] == "X" \
                and board[i][j-1] == "X" \
                and board[i][j+1] == "X":
                board[i][j] = "X"
            else:
                if (i,j) not in explored_so_far:
                    is_surrounded, explored = self.dfs(graph, (i,j), len(board)-1, len(board[0])-1)
                    explored_so_far.update(explored)
                    if is_surrounded:
                        for (i,j) in explored:
                            board[i][j] = "X"

    def dfs(self, graph, start, row_len, col_len):
        explored = set()
        explored.add(start)

        stack = []
        stack.append(start)

        while stack:
            node = stack.pop()
            if node[0] == 0 \
                or node[0] == row_len \
                or node[1] == 0 \
                or node[1] == col_len:
                return False, explored
            for child_node in graph[node]:
                if child_node not in explored:
                    explored.add(child_node)
                    stack.append(child_node)

        return True, explored