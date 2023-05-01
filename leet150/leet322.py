class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #   0 1 2 3 4 5 6 7 8 9 10 11
        # 0 0 m m m m m m m m m m  m
        # 1 0 1 2 3 4 5 6 7 8 9 10 11
        # 2 0 1 1 2 2 3 3 4 4 5 5  6
        # 5 0 1 1 2 2 1 2 2 3 3 2  3

        max_amount = 10001
        dp = []
        for i in range(amount+1):
            dp.append([])
            for _ in range(len(coins)+1):
                dp[i].append(0)

        for i in range(1, amount+1):
            dp[i][0] = max_amount

        for i in range(1, amount+1):
            for j in range(1, len(coins)+1):
                if i >= coins[j-1]:
                    dp[i][j] = min(dp[i][j-1], 1+dp[i-coins[j-1]][j])
                # Amount if less than face value of coin.
                else:
                    dp[i][j] = dp[i][j-1]

        # for i in range(amount+1):
        #     for j in range(len(coins)+1):
        #         print(dp[i][j])
        #     print("---")

        if dp[amount][len(coins)] == max_amount:
            return -1

        return dp[amount][len(coins)]