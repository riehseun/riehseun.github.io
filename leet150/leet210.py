from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Loop through n. Do DFS for each node
        # 1. If a node is pre-requisite for a lot of courses, it will take long to
        # finsh DFS
        # 2. If a node is pre-requisite for only small number of course or even no
        # course, DFS will finish quickly
        # Remember the number of steps taken for DFS starting at each node

        graph = defaultdict(set)

        for edge in prerequisites:
            graph[edge[1]].add(edge[0])

        ordering = []
        for i in range(numCourses):
            count = self.dfs(i, graph)
            # If cycle.
            if count == -1:
                return []
            ordering.append([count, i])

        ordering.sort(key=lambda x:(-x[0]))

        return [item[1] for item in ordering]

    def dfs(self, start_node, graph):
        stack = []
        stack.append(start_node)
        count = 1

        explored = {}
        explored[start_node] = True

        while stack:
            node = stack.pop()
            for next_node in graph[node]:
                if next_node not in explored:
                    explored[next_node] = True
                    stack.append(next_node)
                    count += 1
                else:
                    if next_node == start_node:
                        return -1

        return count