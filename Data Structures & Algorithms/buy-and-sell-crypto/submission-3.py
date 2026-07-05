class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minB = prices[0]

        for d in prices:
            maxP = max(maxP, d-minB)
            minB = min(minB, d)
        return maxP