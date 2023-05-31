from collections import defaultdict, deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Construct a graph.
        # Count number of connnected component using BFS.

        # Connected when a node is 1 and adjacent is also 1.

        graph = defaultdict(list)
        nodes = set()

        n = len(grid)
        m = len(grid[0])
        for i in range(len(grid)):
            for j, num in enumerate(grid[i]):
                if num == "1":
                    if (i,j) not in nodes:
                        nodes.add((i,j))
                    # Check right
                    if j < m-1 and grid[i][j+1] == "1":
                        graph[(i,j)].append((i, j+1))
                        graph[(i,j+1)].append((i,j))  
                    # Check left
                    if j > 0 and grid[i][j-1] == "1":
                        graph[(i,j)].append((i, j-1))
                        graph[(i,j-1)].append((i,j))
                    # Check up
                    if i > 0 and grid[i-1][j] == "1":
                        graph[(i,j)].append((i-1, j))
                        graph[(i-1,j)].append((i,j))
                    # Check down
                    if i < n-1 and grid[i+1][j] == "1":
                        graph[(i,j)].append((i+1, j))
                        graph[(i+1,j)].append((i,j))
                
        explored = set()
        count = 0
        for (i,j) in nodes:
            if (i,j) not in explored:
                self.bfs(graph, explored, (i,j))
                count += 1
        return count

    def bfs(self, graph, explored, start):
        queue = deque()
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(graph[node]) 
            for child_node in graph[node]:          
                if child_node not in explored:
                    explored.add(child_node)
                    queue.append(child_node)