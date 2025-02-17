class Solution:
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        prices.sort()
        res = 0
        for i in range(1, len(prices)):
            if i - 1 >= 0 and i + k <= len(prices):
                res += prices[i] - prices[i-1]
            elif i < k:
                res += prices[k] - prices[0]
            else:
                res += prices[i] - prices[i-k]
        return res