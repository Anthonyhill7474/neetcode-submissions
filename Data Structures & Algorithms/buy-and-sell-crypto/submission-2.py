class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        sell = 1
        while sell < len(prices):
            if (prices[sell] - prices[buy]) > maxProfit:
                maxProfit = (prices[sell] - prices[buy])
            elif prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return maxProfit
