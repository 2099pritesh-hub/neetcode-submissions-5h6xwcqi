class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * (n + 1)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[c] = 1
                elif obstacleGrid[r][c] == 0:
                    dp[c] = dp[c] + dp[c + 1]
                elif obstacleGrid[r][c] == 1:
                    dp[c] = 0
        return dp[0]