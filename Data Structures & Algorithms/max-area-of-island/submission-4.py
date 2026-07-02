class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r, c) in visit:
                return 0
            
            visit.add((r, c))
            area = 1
            for dr, dc in neighbors:
                area += dfs(r + dr, c + dc)
            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c))
        return res