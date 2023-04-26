from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Each element in prerequisites is two nodes in directed graph
        # If cycle, return False

        directed_graph = defaultdict(list)

        # Time O(m) where m is number of edges in graph.
        # Space O(n) where n is number of nodes in graph.
        for pair in prerequisites:
            directed_graph[pair[1]].append(pair[0])

        # Time O(n^2)
        for node in directed_graph:
            if self.dfs(node, directed_graph):
                return False

        return True

    # DFS.
    # Time O(n+m) where n is number of nodes and m is number of edges in graph.
    # Space O(n)
    def dfs(self, start_node, directed_graph):
        explored = {}
        explored[start_node] = True

        stack = []
        stack.append(start_node)

        is_cycle = False

        while stack:
            node = stack.pop()
            if node in directed_graph:
                for next_node in directed_graph[node]:
                    if next_node not in explored:
                        explored[next_node] = True
                        stack.append(next_node)
                    else:
                        if next_node == start_node:
                            is_cycle = True

        return is_cycle