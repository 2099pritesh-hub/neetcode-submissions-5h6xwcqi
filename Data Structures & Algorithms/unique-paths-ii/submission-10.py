class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * (n + 1)
        
        for r in range(m - 1, -1, -1):
            cur = [0] * (n + 1)
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    cur[c] = 0
                    continue
                if r == (m - 1) and c == (n - 1):
                    cur[c] = 1
                    continue
                cur[c] = prev[c] + cur[c + 1]
            prev = cur
        return prev[0]