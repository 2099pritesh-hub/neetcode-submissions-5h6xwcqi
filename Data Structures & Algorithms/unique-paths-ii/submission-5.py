class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                down = dp[r + 1][c] if r + 1 < ROWS else 0
                right = dp[r][c + 1] if c + 1 < COLS else 0

                dp[r][c] = down + right
        return dp[0][0]