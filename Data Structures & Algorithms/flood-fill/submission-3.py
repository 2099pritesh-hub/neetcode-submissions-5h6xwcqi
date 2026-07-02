class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixelColor = image[sr][sc]
        if pixelColor == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                image[r][c] != pixelColor):
                return
            
            image[r][c] = color
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image          