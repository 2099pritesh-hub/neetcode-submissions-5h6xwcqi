class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        minute = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbors:
                    if (r + dr >= ROWS or c + dc >= COLS or min(r + dr, c + dc) < 0 or
                        grid[r + dr][c + dc] != 1):
                        continue
                    grid[r + dr][c + dc] = 2
                    fresh -= 1
                    queue.append((r + dr, c + dc))
            if queue:
                minute += 1
        
        return minute if fresh == 0 else -1