class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Each cell container the number of unique path leading
        # up to it. The value at a cell is the addition of its left
        # and up cell.
        #   0 1 2 3 4 5 6 7
        # 0 0 0 0 0 0 0 0 0
        # 1 0 1 1 1 1 1 1 1
        # 2 0 1 2 3 4 5 6 7
        # 3 0 1 3 6 10 15 21 28 

        dp = []
        for i in range(m+1):
            dp.append([])
            for _ in range(n+1):
                dp[i].append(0)

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]