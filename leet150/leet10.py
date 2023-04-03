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

        # First row for a pattern to match an empty char in string.
        for j in range(1, len(p)+1):
            # For * to match an empty string, everything up to the last
            # two characters needs to match and the preceeding char
            # can be anything.
            if p[j-1] == "*":
                if dp[0][j-2] == "Y":
                    dp[0][j] = "Y"
                else:
                    dp[0][j] = "N"
            else:
                dp[0][j] = "N"

        # First column for an empty char in pattern to match any char
        # in string.
        for i in range(1, len(s)+1):
            dp[i][0] = "N"

        # for i in range(0, len(s)+1):
        #     for j in range(0, len(p)+1):
        #         print(dp[i][j])
        #     print("\n")

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                # If two characters match, Then two substrings
                # without these two characters will be the result.
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == "*":
                        # In this case, p[j-2] is important.
                        # This mean any character is repeated zero
                        # or more times, so the pattern will match
                        # all possible scenarios.

                        #       . * . . a *
                        #     0 1 2 3 4 5 6
                        #   0 Y N Y N N N N
                        # a 1 N Y Y Y N N N
                        if p[j-2] == s[i-1] or p[j-2] == ".":
                            if (dp[i][j-2] == "Y" \
                                or dp[i-1][j-2] == "Y" \
                                or dp[i-1][j] == "Y"):
                                # One of three conditions satisfied.
                                dp[i][j] = "Y"
                            else:
                                dp[i][j] = "N"
                        else:
                            dp[i][j] = dp[i][j-2]
                    # In this case, pattern can be any character to
                    # satisfy this condition: s[j-1] == p[j-1]
                    elif p[j-1] == ".":
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = "N"

        # for i in range(0, len(s)+1):
        #     for j in range(0, len(p)+1):
        #         print(dp[i][j])
        #     print("\n")

        if dp[len(s)][len(p)] == "Y":
            return True
        else:
            return False