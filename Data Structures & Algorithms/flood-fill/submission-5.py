class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialColor = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != initialColor or 
                image[r][c] == color):
                return
            
            image[r][c] = color
            for dr, dc in neighbors:
                dfs(dr + r, dc + c)
            
        dfs(sr, sc)
        return image