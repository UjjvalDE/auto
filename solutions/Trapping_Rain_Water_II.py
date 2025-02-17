class Solution:
    def trapRainWater(self, heightMap):
        m, n = len(heightMap), len(heightMap[0])
        pq = [(heightMap[i][0], i, 0) for i in range(m)] + [(heightMap[i][n-1], i, n-1) for i in range(m)]
        res = 0
        while pq:
            h, x, y = heapq.heappop(pq)
            if y+1 < n and heightMap[x][y+1] <= h:
                res += (h - heightMap[x][y+1])
            if x+1 < m and heightMap[x+1][y] <= h:
                res += (h - heightMap[x+1][y])
            if pq:
                heapq.heappush(pq, (max(h, heightMap[min(x+1, m-1)][min(y+1, n-1)]), min(x+1, m-1), min(y+1, n-1)))
        return res