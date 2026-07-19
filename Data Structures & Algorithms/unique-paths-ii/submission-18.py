class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (n + 1)

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1 and obstacleGrid[r][c] == 0:
                    dp[c] = 1
                    continue
                dp[c] = dp[c] + dp[c + 1] if obstacleGrid[r][c] == 0 else 0
        return dp[0]