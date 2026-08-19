class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        empty_board = [
            ["." for _ in range(n) ] for _ in range(n)
        ]

        result = []

        def is_valid_queen(board, row, i):
            if 'Q' in board[row]:
                return False

            for r in board:
                if r[i] == 'Q':
                    return False
            
            curr_i = i
            curr_row = row
            while curr_i < len(board) and curr_row > -1:
                if board[curr_row][curr_i] == 'Q':
                    return False
                curr_i += 1
                curr_row -= 1
            
            curr_i = i
            curr_row = row
            while curr_i > -1 and curr_row > -1:
                if board[curr_row][curr_i] == 'Q':
                    return False
                curr_i -= 1
                curr_row -= 1
            
            return True
            

        def dfs_bt(board, row, queens):
            nonlocal result

            if queens == len(board):
                result.append([''.join(row) for row in board])
                return
            
            for i in range(len(board)):
                if is_valid_queen(board, row, i):
                    board[row][i] = 'Q'
                    dfs_bt(board, row + 1, queens + 1)
                    board[row][i] = '.'
            

        dfs_bt(empty_board, 0, 0)
        return result