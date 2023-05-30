class Solution:
    def trailingZeroes(self, n: int) -> int:

        # Number of 0 = min(number of 2, number of 5)
        # There are more 2 than 5, so focus on 5 only.

        count = 0

        while n > 0:
            count += int(n/5)
            n /= 5

        return count