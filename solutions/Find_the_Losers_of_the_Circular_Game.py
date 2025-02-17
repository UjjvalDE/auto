class Solution:
    def circularGameLosers(self, n: int, players: List[int]) -> List[str]:
        players.sort()
        losers = []
        for i in range(n - 1):
            if players[i + 1] > 2 * players[i] - 1:
                losers.append(chr(ord('A') + i))
        return losers