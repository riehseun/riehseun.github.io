from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        graph = defaultdict(list)
        word_list = [beginWord] + wordList
        # word_list = set(word_list)
        all_possible_word = defaultdict(set)

        for word in word_list:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    all_possible_word[word].add(word[:i]+c+word[i+1:])

        for i in range(len(word_list)):
            for j in range(i+1, len(word_list)):
                if word_list[j] in all_possible_word[word_list[i]]:
                    graph[word_list[i]].append(word_list[j])
                    graph[word_list[j]].append(word_list[i])

        return self.bfs(graph, beginWord, endWord)

    def bfs(self, graph, start, end):
        explored = set()
        explored.add(start)

        queue = deque()
        queue.append((start, 1))

        while queue:
            node, depth = queue.popleft()
            for child_node in graph[node]:
                if child_node == end:
                    return depth+1

                if child_node not in explored:
                    explored.add(child_node)
                    queue.append((child_node, depth+1))

        return 0