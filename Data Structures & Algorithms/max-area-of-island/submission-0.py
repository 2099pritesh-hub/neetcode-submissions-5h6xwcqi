class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            area = 1
            grid[r][c] = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i, j), maxArea)
        
        return maxArea