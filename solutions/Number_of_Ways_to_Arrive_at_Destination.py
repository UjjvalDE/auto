class Solution:
    def countPaths(self, n: int, roads: List[List[int]], traps: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for road in roads:
            graph[road[0]].append((road[1], 1))
            graph[road[1]].append((road[0], 1))
        MOD = 10**9 + 7
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if i not in traps:
                for j in graph[i]:
                    dp[i] += dp[j[0]]
                    dp[i] %= MOD
        return sum(dp)