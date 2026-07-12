class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for word in strs:
            words.append(str(len(word)) + "#" + word)
        return "".join(words)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        number = 0

        while i < len(s):
            if s[i] == '#':
                length = int(s[number:i])
                word = s[i+1: i+1+length]
                words.append(word)
                i += length+1
                number = i
            else:
                i += 1
        return words