from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def are_valid_indices(x, y) -> bool:
            return x < rows and x > -1 and y < cols and y > -1
        
        def is_on_edge(x, y) -> bool:
            return x == 0 or x == rows - 1 or y == 0 or y == cols - 1

        def bfs(i: int, j: int) -> bool:
            visited.add((i, j))

            index_pairs = [(i, j)]
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                if is_on_edge(x, y):
                    return False, index_pairs

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if are_valid_indices(nx, ny) and board[nx][ny] == 'O' and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        index_pairs.append((nx, ny))
            
            return True, index_pairs

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    visited = set()
                    surroundable, index_pairs = bfs(i, j)
                    if surroundable:
                        for x, y in index_pairs:
                            board[x][y] = 'X'