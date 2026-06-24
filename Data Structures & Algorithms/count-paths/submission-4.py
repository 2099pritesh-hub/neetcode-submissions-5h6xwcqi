class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        
        for r in range(m - 1, -1, -1):
            curCol = [0] * n
            curCol[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curCol[c] = prevRow[c] + curCol[c + 1]
            prevRow = curCol
        return prevRow[0]