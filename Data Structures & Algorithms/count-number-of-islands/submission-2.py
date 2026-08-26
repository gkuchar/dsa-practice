class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def search(i: int, j: int, grid: List[List[str]]) -> None:

            grid[i][j] = '2' # mark as visited
            directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

            def are_valid_indicies(x: int, y: int) -> bool:
                return x > -1 and x < rows and y > -1 and y < cols

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if are_valid_indicies(x, y) and grid[x][y] == '1':
                    search(x, y, grid)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    search(i, j, grid)
                    islands += 1
        
        return islands
        # T = O(n * m), n = # rows, m = # cols
        # S = O(l), l = size of largest island: space allocated on call stack from recursion 
        