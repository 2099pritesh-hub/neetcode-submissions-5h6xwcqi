class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != original:
                return
            
            image[r][c] = color
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image