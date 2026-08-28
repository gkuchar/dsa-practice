class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        can_access = [[[False, False] for _ in range(cols)] for _ in range(rows)]
        result = []

        def are_valid_indices(x, y):
            return x > -1 and x < rows and y > -1 and y < cols

        # find all cells pacific can reach
        q = deque()
        seen = set()
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # seed the q with top row and left-most column (they always can reach pacific)
        for i in range(rows):
            q.append((i, 0))
            seen.add((i, 0))
        for j in range(cols):
            q.append((0, j))
            seen.add((0, j))


        while q:
            x, y = q.popleft()
            can_access[x][y][0] = True

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # new cells can also reach pacific from current cell if new cell height is >= current cell height
                if are_valid_indices(nx, ny) and (nx, ny) not in seen and heights[nx][ny] >= heights[x][y]:
                    q.append((nx, ny))
                    seen.add((nx, ny))
        
        # find all cells atlantic can reach
        q = deque()
        seen = set()

        # seed the q with bottom row and right-most column (they always can reach atlantic)
        for i in range(rows):
            q.append((i, cols - 1))
            seen.add((i, cols - 1))
        for j in range(cols):
            q.append((rows - 1, j))
            seen.add((rows - 1, j))


        while q:
            x, y = q.popleft()
            can_access[x][y][1] = True

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # new cells can also reach atlantic from current cell if new cell height is >= current cell height
                if are_valid_indices(nx, ny) and (nx, ny) not in seen and heights[nx][ny] >= heights[x][y]:
                    q.append((nx, ny))
                    seen.add((nx, ny))
        
        # include all cells that both the pacific and atlantic can reach
        for i in range(rows):
            for j in range(cols):
                if can_access[i][j][0] and can_access[i][j][1]:
                    result.append([i, j])
        
        return result
        # T = O(n * m)
        # S = O(n * m)
        