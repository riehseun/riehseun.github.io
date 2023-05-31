class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        return self.helper(n, seen)

    def helper(self, n, seen):
        
        if n == 1:
            return True

        if n in seen:
            return False

        num = 0
        for char in str(n):
            num += int(char) ** 2
        seen.add(n)

        return self.helper(num, seen)