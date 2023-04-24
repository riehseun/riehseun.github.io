class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0
        profit = 0

        while buy < len(prices) and sell < len(prices):
            while buy < len(prices)-1 and prices[buy+1] < prices[buy]:
                buy += 1

            sell = buy

            while sell < len(prices)-1 and prices[sell+1] > prices[sell]:
                sell += 1

            profit += prices[sell] - prices[buy]
            buy = sell + 1

        return profit