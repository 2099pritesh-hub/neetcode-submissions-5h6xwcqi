class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    if obstacleGrid[r][c] == 0:
                        dp[r][c] = 1
                elif obstacleGrid[r][c] == 0:
                    below = dp[r + 1][c] if r + 1 < m else 0
                    right = dp[r][c + 1] if c + 1 < n else 0
                    dp[r][c] = below + right

        return dp[0][0]