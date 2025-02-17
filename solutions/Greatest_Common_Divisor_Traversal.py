class Solution:
    def findGCD(self, nums):
        from math import gcd
        return gcd(reduce(lambda x, y: abs(x) | abs(y), nums)) if nums else 0