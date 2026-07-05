class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        length = len(prices)
        while left < right and right < length:
            if (prices[right] < prices[left]):
                left = right
            else:
                if (prices[right] - prices[left]) > profit:
                    profit = (prices[right] - prices[left])
            right +=1
        return profit