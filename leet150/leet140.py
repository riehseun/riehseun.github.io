class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # dp[i] = all possible outputs for s[:i+1]
        word_set = set(wordDict)
        n = len(s)

        dp = []
        for i in range(n):
            dp.append([])
        dp += [[""]]

        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:i+1] in word_set:
                    for sol in dp[j-1]:
                        dp[i].append(sol+" "+s[j:i+1])

        result = []
        for string in dp[n-1]:
            if len(string.strip().replace(" ", "")) == n:
                result.append(string.strip())

        return result