class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        rows = len(grid)
        cols = len(grid[0])

        def search(i: int, j: int) -> int:
            size = 1
            grid[i][j] = 2
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            def are_valid_indicies(x, y):
                return x > -1 and x < rows and y > -1 and y < cols
            
            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if are_valid_indicies(x, y) and grid[x][y] == 1:
                    size += search(x, y)
            
            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = search(i, j)
                    largest = max(largest, size)
        
        return largest