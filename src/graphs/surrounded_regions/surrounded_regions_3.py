from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        bad_indices = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def are_valid_indices(x, y) -> bool:
            return x < rows and x > -1 and y < cols and y > -1
        
        def is_on_edge(x, y) -> bool:
            return x == 0 or x == rows - 1 or y == 0 or y == cols - 1

        def bfs(i: int, j: int) -> bool:
            surroundable = True
            visited.add((i, j))

            index_pairs = [(i, j)]
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                if is_on_edge(x, y):
                    surroundable = False

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in bad_indices:
                        return False, []

                    if are_valid_indices(nx, ny) and board[nx][ny] == 'O' and (nx, ny) not in visited:

                        q.append((nx, ny))
                        visited.add((nx, ny))
                        index_pairs.append((nx, ny))
            
            return surroundable, index_pairs

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    visited = set()
                    surroundable, index_pairs = bfs(i, j)
                    if surroundable:
                        for x, y in index_pairs:
                            board[x][y] = 'X'
                    else:
                        for x, y in index_pairs:
                            bad_indices.add((x, y))
        # T = O(n * m)
        # S = O(n * m)