class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:            
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            time += 1

        return time if not fresh else -1