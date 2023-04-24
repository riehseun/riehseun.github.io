class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = 0
        end = 0
        max_profit = 0

        while start <= end and end < len(prices):

            diff = prices[end] - prices[start]
            max_profit = max(max_profit, diff)

            if diff <= 0:
                start = end
            end += 1

        return max_profit