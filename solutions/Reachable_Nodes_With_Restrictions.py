class Solution:
    def reachableNodes(self, n: int, restrictions: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in restrictions:
            graph[a].append(b)
            graph[b].append(a)

        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]
            if not graph[node]:
                return 0
            res = 1
            for neighbor in graph[node]:
                res += dfs(neighbor)
            memo[node] = res
            return res

        ans = 0
        for i in range(n):
            ans += dfs(i) - 1
        return ans