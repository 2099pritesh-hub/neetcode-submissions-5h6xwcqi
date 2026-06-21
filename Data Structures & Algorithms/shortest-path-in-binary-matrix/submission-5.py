class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
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
                
                for dr, dc in neighbors:
                    ndr, ndc = r + dr, c + dc
                    if (min(ndr, ndc) < 0 or ndr >= ROWS or ndc >= COLS or
                        (ndr, ndc) in visit or grid[ndr][ndc] != 0):
                        continue
                    queue.append((ndr, ndc))
                    visit.add((ndr, ndc))
            length += 1
        return -1