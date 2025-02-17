def maxAlternatingSum(self, grid):
    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        curr_sum = 0
        for j in range(n):
            if (i + j) % 2 == 0:
                curr_sum += max(0, grid[i][j])
            else:
                curr_sum -= min(0, grid[i][j])
        res = max(res, curr_sum)
    return res