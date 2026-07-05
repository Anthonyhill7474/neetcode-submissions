from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        for ch in t:
            if seen.get(ch, 0) == 0:
                return False
            else:
                seen[ch] -= 1
        return True