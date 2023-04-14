from heapq import heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        # dp[t] = furthest distance we can travel with fueling t times.
        # Then, dp[t+1] = max(dp[t+1], dp[t]+stations[i][1])

        # start = 10, target = 100, [10,60],[20,30],[30,30],[60,40]
        # 0  1  2  3  4
        # 10 70 110

        if startFuel >= target:
            return 0

        if not stations:
            return -1

        n = len(stations)
        dp = [startFuel] + [0] * n

        for i in range(n):
            for t in range(i, -1, -1):
                if dp[t] >= stations[i][0] and t != n:
                    dp[t+1] = max(dp[t+1], dp[t]+stations[i][1])

        for t, d in enumerate(dp):
            if d >= target:
                return t

        return -1

