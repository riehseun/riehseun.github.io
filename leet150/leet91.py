class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to parse the string s[:i]
        # s = "231"
        # dp[0] = 1
        # "2" dp[1] = 1
        # "23" dp[2] = 2
        # "231" dp[3] = 2

        #     2 3 1
        #   1 1 2 2

        dp = []
        for i in range(len(s)+1):
            dp.append(0)

        dp[0] = 1 
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s)+1): 
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]

            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        for i in dp:
            print(i)

        return dp[len(s)]
        