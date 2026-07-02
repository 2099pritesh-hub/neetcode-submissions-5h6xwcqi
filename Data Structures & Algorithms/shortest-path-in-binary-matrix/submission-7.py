class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
            
        n = len(grid)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))

        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or max(nr, nc) == n or
                        grid[nr][nc] != 0 or (nr, nc) in visit):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1