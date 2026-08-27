from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def are_valid_indices(x, y):
            return x < rows and x > -1 and y < cols and y > -1

        def bfs_search(q, visited):
            distance = 0

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()

                    if grid[x][y] == -1:
                        continue
                    
                    grid[x][y] = distance
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if are_valid_indices(nx, ny) and (nx, ny) not in visited:
                            q.append((nx, ny))
                            visited.add((nx, ny))
                distance += 1
            
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i,j))
        bfs_search(q, visited)
        # T = O(V), V = n * m
        # S = O(V),

        