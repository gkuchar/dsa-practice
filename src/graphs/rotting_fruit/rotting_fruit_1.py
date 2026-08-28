from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        def count_fruits(grid):
            fresh = 0

            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        fresh += 1
                    elif grid[i][j] == 2:
                        q.append((i, j))
            
            return fresh
        
        def are_valid_indicies(x, y):
            return x < rows and x > -1 and y < cols and y > -1

        def spread_rot(grid, q, fresh):
            remaining = fresh
            minutes = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
                        if are_valid_indicies(nx, ny) and grid[nx][ny] == 1:
                            q.append((nx, ny))
                            grid[nx][ny] = 2
                            remaining -= 1
                if q: minutes += 1
            
            return minutes, remaining
        
        fresh = count_fruits(grid)

        minutes, remaining = spread_rot(grid, q, fresh)

        return minutes if remaining == 0 else -1
        # T = O(n * m)
        # S = O(n * m)