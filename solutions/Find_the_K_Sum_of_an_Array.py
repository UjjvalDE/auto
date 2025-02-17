class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        total_sum = sum(nums)
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(min(i, k), -1, -1):
                for m in range(j):
                    if prefix_sum[i] - prefix_sum[m] >= total_sum - (k - 1) * MOD:
                        dp[i][j] += dp[m][j - 1]
                        dp[i][j] %= MOD
        return dp[n][k]