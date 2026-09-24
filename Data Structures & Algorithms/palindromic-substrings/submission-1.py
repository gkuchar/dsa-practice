class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        

        palins = 0
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                if dp[start][end]:
                    palins += 1
                    continue
                
                if s[start] == s[end] and (end - start + 1 <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    palins += 1
        
        return palins
        # T = O(n^2)
        # S = O(n^2)
                
