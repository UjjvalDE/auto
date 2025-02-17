class Solution:
    def minOperations(self, target: List[int], start: int, end: int) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n):
            if target[i] > start:
                dp[i] = min(dp[i], 1 + dp[i - 1])
            if target[i] < end and target[i] <= start:
                dp[i] = min(dp[i], 1 + dp[i - 1])
        return dp[n - 1] if dp[n - 1] != float('inf') else -1