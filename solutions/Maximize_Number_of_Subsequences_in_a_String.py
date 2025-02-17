class Solution:
    def maxSubsequenceCount(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        n = len(s)
        p = [1] * (n + 1)
        for i in range(1, n):
            p[i] = (p[i - 1] << 1) % MOD
            if s[i] != s[i - 1]:
                res += p[i]
        return res