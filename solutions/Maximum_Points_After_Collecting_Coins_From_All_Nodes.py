class Solution:
    def maxPoints(self, coins: List[List[int]]) -> int:
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(i):
                if i - j > 1 and i % (i - j) == 0:
                    dp[i][j] = max(dp[j][j - 1] + sum(coins[k][i-1] for k in range(j)), 
                                   dp[j][j-1])
                else: 
                    dp[i][j] = max(dp[j][j-1] + sum(coins[k][i-1] for k in range(j)) if j > 0 else 0, 
                                   dp[j+1][i-1] if i - j > 1 else dp[j][i-1])
        return dp[-1][-1]