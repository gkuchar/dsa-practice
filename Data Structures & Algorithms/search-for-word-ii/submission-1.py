class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie from words
        # dfs on each cell in grid, traversing trie in lockstep
        # only continue dfs if next char is in trie curr_layer
        # if reach end of word (marked by word field), append word

        def build_trie(words):
            main = {}
            for word in words:
                curr_layer = main
                for char in word:
                    if char not in curr_layer:
                        curr_layer[char] = {}
                    curr_layer = curr_layer[char]
                curr_layer['word'] = word
            
            return main
        
        main = build_trie(words)
        rows = len(board)
        cols = len(board[0])
        result = set()
        
        def dfs(row, col, curr_layer, visited):
            nonlocal result

            if not (row < rows and row >= 0 and col < cols and col >= 0):
                return
            
            if (row, col) in visited:
                return
            
            curr_char = board[row][col]
            if curr_char not in curr_layer:
                return
            
            if 'word' in curr_layer[curr_char]:
                result.add(curr_layer[curr_char]['word'])
            
            visited.add((row, col))
            
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]

            for x, y in directions:
                dfs(row + x, col + y, curr_layer[curr_char], visited)
            visited.remove((row, col)) 
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, main, set())
        
        return list(result)
        