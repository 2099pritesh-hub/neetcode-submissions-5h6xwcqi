class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iColor = image[sr][sc]
        if iColor == color:
            return image
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != iColor:
                return
            
            image[r][c] = color
            neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in neighbours:
                dfs(dr + r, dc + c)
            
        dfs(sr, sc)
        return image