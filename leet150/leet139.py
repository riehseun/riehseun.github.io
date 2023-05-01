from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        occurences = defaultdict(list)

        for word in wordDict:

            start = 0
            end = len(s)
            while start < end:
                index = s.find(word, start, end)
                if index == -1:
                    break
                else:
                    occurences[index].append(index+len(word))
                    start = index + 1

        return self.dfs(occurences, 0, len(s))


    def dfs(self, graph, start_node, end_node):
        explored = set()
        explored.add(start_node)

        stack = []
        stack.append(start_node)

        while stack:
            node = stack.pop()
            if node in graph:
                for child_node in graph[node]:
                    if child_node == end_node:
                        return True

                    if child_node not in explored:
                        stack.append(child_node)
                        explored.add(child_node)

        return False