class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = "".join(char for char in s if char.isalnum()).lower().strip()
        return test == test[::-1]