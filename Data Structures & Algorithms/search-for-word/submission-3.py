class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(path, i, j, wix):
            nonlocal board
            nonlocal word

            if (i, j) in path: return
            if i < 0 or i >= len(board): return
            if j < 0 or j >= len(board[0]): return

            if board[i][j] != word[wix]:
                return

            if wix + 1 == len(word):
                return True
            
            
            path.add((i, j))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                ix = i + dx
                jx = j + dy

                if search(path, ix, jx, wix + 1):
                    return True

            if path: path.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                found = search(set(), i, j, 0)
                if found:
                    return True
        
        return False