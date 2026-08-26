class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def search(i: int, j: int) -> None:
            nonlocal seen

            seen.add((i, j))
            directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

            def are_valid_indicies(x: int, y: int) -> bool:
                return x > -1 and x < rows and y > -1 and y < cols

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if are_valid_indicies(x, y) and grid[x][y] == '1' and (x, y) not in seen:
                    search(x, y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in seen:
                    search(i, j)
                    islands += 1
        
        return islands
        