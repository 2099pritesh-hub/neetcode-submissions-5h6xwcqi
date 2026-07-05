class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for r in range(m - 2, -1, -1):
            cur = [1] * n
            for c in range(n - 2, -1, -1):
                cur[c] = prev[c] + cur[c + 1]
            prev = cur
        return prev[0]