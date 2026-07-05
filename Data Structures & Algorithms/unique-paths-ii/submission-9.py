class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r == (m - 1) and c == (n - 1):
                    dp[r][c] = 1
                    continue
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]