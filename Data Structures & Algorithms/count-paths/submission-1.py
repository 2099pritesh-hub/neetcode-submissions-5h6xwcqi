class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        def dfs(r, c, cache):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            if r == ROWS or c == COLS:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            count = 0
            neighbors = [(1, 0), (0, 1)]
            for dr, dc in neighbors:
                count += dfs(r + dr, c + dc, cache)
            cache[(r, c)] = count
            return count
        
        return dfs(0, 0, {})