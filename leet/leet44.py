class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Initialize 2D array.
        dp = []
        for i in range(0, len(s)+1):
            dp.append([])
            for j in range(0, len(p)+1):
                dp[i].append(" ")

        # An empty pattern always mathes an empty string.
        dp[0][0] = "Y"

        #       a a b a a a
        #     0 1 2 3 4 5 6
        #   0 Y N N N N N N
        # a 1 N Y N N N N N
        # * 2 Y Y Y N N N N
        # ? 3 Y Y N N N N N

        # First row for a pattern to match an empty char in string.
        for i in range(1, len(s)+1):
            dp[i][0] = "N"

        # First column for an empty char in pattern to match any char
        # in string.
        for j in range(1, len(p)+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = "N"

        # for i in range(0, len(s)+1):
        #     for j in range(0, len(p)+1):
        #         print(dp[i][j])
        #     print("\n")

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if dp[i-1][j] == "Y" or dp[i][j-1] == "Y":
                        dp[i][j] = "Y"
                    else:
                        dp[i][j] = "N"
                else:
                    dp[i][j] = "N"

        for i in range(0, len(s)+1):
            for j in range(0, len(p)+1):
                print(dp[i][j])
            print("\n")

        if dp[len(s)][len(p)] == "Y":
            return True
        else:
            return False