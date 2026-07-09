class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0, 0
        count = {}
        maxCount = 0
        res = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            maxCount = max(maxCount, count[s[j]])

            while (j - i + 1) - maxCount > k:
                count[s[i]] -= 1
                i += 1
            
            res = max(res, j-i+1)
        return res