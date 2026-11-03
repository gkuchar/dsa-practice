class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if m > n: return 0

        memo = {}

        def compute(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                memo[(i, j)] = 1
                return 1

            if i == n:
                memo[(i, j)] = 0
                return 0
            
            ways_include = compute(i + 1, j + 1) if s[i] == t[j] else 0
            ways_not_include = compute(i + 1, j)

            memo[(i, j)] = ways_include + ways_not_include
            return ways_include + ways_not_include
        
        return compute(0, 0)
        # T = O(n * m)
        # S = O(n * m)