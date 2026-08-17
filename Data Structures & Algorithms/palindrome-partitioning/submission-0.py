class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palin(sub):
            l = 0
            r = len(sub) - 1

            while l < r:
                if sub[l] != sub[r]: return False
                l += 1
                r -= 1
            
            return True

        def dfs_bt(start, path):
            nonlocal result
            nonlocal s

            if start == len(s):
                result.append(path[:])
            
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if is_palin(piece):
                    path.append(piece)
                    dfs_bt(end, path)
                    path.pop()
                
        
        dfs_bt(0, [])
        return result