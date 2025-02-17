class Solution:
    def subarrayBits(self, arr):
        n = len(arr)
        res = 0
        for i in range(32):
            cnt1 = sum((x >> i) & 1 for x in arr)
            res |= (cnt1 << i)
        return res