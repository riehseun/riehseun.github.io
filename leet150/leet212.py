from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.num_words = 0
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: 

        if not board:
            return []

        n = len(board)  # row.
        m = len(board[0])  # col.
        result = []
        
        trie = Trie()
        trie.num_words = len(words)
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(n):
            for j in range(m):
                self.helper(board, result, trie, node, i, j, n, m, "")
                          
        return result

    def helper(self, board, result, trie, node, i, j, n, m, path):

        if trie.num_words == 0:
            return

        if node.is_word:
            result.append(path)
            trie.num_words -= 1
            node.is_word = False
            
        if 0 <= i < n and 0 <= j < m:
            temp = board[i][j]
            node = node.children.get(temp)
            if not node:
                return

            board[i][j] = "#"
            self.helper(board, result, trie, node, i+1, j, n, m, path+temp)
            self.helper(board, result, trie, node, i-1, j, n, m, path+temp)
            self.helper(board, result, trie, node, i, j+1, n, m, path+temp)
            self.helper(board, result, trie, node, i, j-1, n, m, path+temp)
            board[i][j] = temp 

        else:
            return

        return False