class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1" or (r, c) in visit:
                return
            
            visit.add((r, c))
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1
        return count