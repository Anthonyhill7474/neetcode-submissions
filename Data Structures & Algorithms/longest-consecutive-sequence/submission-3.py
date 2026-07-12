class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set()
        maximum = float("-inf")
        minimum = float("inf")
        for num in nums:
            seen.add(num)
            maximum = max(maximum, num)
            minimum = min(minimum, num)
        
        count = 0 
        maxCount = 0
        i = 0
        for i in range(minimum, maximum+1):
            if i in seen:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0

        return maxCount
        