class Solution:
    def countSubstrings(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                if all(k in word for k in word[i:j]):
                    res += 1
        return res