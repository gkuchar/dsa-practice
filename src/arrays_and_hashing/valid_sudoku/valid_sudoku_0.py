class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = {i : set() for i in range(9)}
        col_sets = {i : set() for i in range(9)}
        sub_box_sets = {i : set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.': continue
                if curr in row_sets[i]:
                    return False
                row_sets[i].add(curr)

                if curr in col_sets[j]:
                    return False
                col_sets[j].add(curr)

                sub_box_row = i // 3
                sub_box_col = j // 3

                sub_box_idx = sub_box_row * 3 + sub_box_col

                if curr in sub_box_sets[sub_box_idx]:
                    return False
                sub_box_sets[sub_box_idx].add(curr)        
        
        return True

        # T = O(1)
        # S = O(1)