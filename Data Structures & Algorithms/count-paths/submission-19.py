class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                row[c] = row[c] + row[c + 1]
        return row[0]