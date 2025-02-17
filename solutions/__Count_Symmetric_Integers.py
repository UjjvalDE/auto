class Solution:
    def countSymmetricIntegers(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            s = str(i)
            if s == s[::-1]:
                res += 1
        return res