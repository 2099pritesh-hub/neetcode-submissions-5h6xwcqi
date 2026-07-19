class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n 

        for r in range(m - 2, - 1, -1):
            curRow = [1] * n
            for c in range(n - 2, -1, -1):
                curRow[c] = prevRow[c] + curRow[c + 1]
            prevRow = curRow
        return prevRow[0]