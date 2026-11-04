class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = {}

        def recurse(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                ops = n - i
                memo[(i, j)] = ops
                return ops
            
            if i == n:
                ops = m - j
                memo[(i, j)] = ops
                return ops
            
            if word1[i] == word2[j]:
                ops = recurse(i + 1, j + 1)
                memo[(i, j)] = ops
                return ops
            
            remove = recurse(i + 1, j) + 1

            insert = recurse(i, j + 1) + 1

            replace = recurse(i + 1, j + 1) + 1

            ops = min(remove, insert, replace)
            memo[(i, j)] = ops
            return ops
        
        return recurse(0, 0)
        # T = O(n * m)
        # S = O(n * m)