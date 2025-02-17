class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        i = len(piles) - 2
        while i >= 0:
            if i % 2 == 1:
                coins += piles[i] + 1
            i -= 1
        return coins