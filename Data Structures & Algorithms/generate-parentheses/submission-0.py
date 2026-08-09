class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs_bt(path, opens_left, closed_left):
            if len(path) == n * 2:
                string = ''.join(path)
                result.append(string)
                return
            
            if len(path) == 0:
                path.append("(")
                dfs_bt(path, opens_left - 1, closed_left)
                return
            
            if opens_left > 0:
                path.append("(")
                dfs_bt(path, opens_left - 1, closed_left)
                path.pop()

            if opens_left < closed_left: 
                path.append(")")
                dfs_bt(path, opens_left, closed_left - 1)
                path.pop()
        
        dfs_bt([], n, n)

        return result
            