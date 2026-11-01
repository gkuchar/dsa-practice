class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maxx = 1

        lengths = [[0] * m for _ in range(n)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def valid_indices(x, y):
            return x > -1 and x < n and y > -1 and y < m

        def get_longest(i, j):
            nonlocal maxx

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if not valid_indices(x, y):
                    continue

                if matrix[x][y] > matrix[i][j]:
                    if lengths[x][y] == 0:
                        get_longest(x, y)

                    lengths[i][j] = max(lengths[i][j], lengths[x][y] + 1)
                    maxx = max(maxx, lengths[i][j])

            if lengths[i][j] == 0:
                lengths[i][j] = 1
            
        for i in range(n):
            for j in range(m):
                if lengths[i][j] == 0:
                    get_longest(i, j)
        
        return maxx
        # T = O(n * m)
        # S = O(n * m)
        
