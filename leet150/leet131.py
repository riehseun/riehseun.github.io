class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.helper(s, [], 1, result)
        return result

    def helper(self, s, path, i, result):
        if i == len(s) + 1:
            result.append(list(path))
            return
        for j in range(i, len(s)+1):
            if self.is_palindrome(s[i-1:j]):
                path.append(s[i-1:j])
                self.helper(s, path, j+1, result)
                path.pop()

    def is_palindrome(self, x):
        return x == x[::-1]