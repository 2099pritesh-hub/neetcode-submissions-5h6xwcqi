class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS = COLS = len(grid)
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
            
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
                for dr, dc in neighbors:
                    if (min(dr + r, dc + c) < 0 or
                        dr + r == ROWS or dc + c == COLS or 
                        (dr + r, dc + c) in visit or grid[dr + r][dc + c] == 1):
                        continue
                    queue.append((dr + r, dc + c))
                    visit.add((dr + r, dc + c))
            length += 1
        return -1