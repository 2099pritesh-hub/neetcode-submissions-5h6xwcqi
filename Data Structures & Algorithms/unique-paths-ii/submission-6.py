class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        prevRow = [0] * COLS

        for r in range(ROWS - 1, -1, -1):
            newRow = [0] * COLS
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    newRow[c] = 1
                    continue
                if obstacleGrid[r][c] == 1:
                    newRow[c] = 0
                    continue
                down = prevRow[c]
                right = newRow[c + 1] if c + 1 < COLS else 0

                newRow[c] = down + right
            prevRow = newRow
        return prevRow[0]