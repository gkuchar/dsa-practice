class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        def count_decoding(i):
            if i in dp:
                return dp[i]

            if i >= n:
                return 1
            
            count = 0
            if s[i] != '0':
                count += count_decoding(i + 1)
            if i + 1 < n and s[i] != '0' and int(s[i:i + 2]) < 27:
                count += count_decoding(i + 2)
            
            dp[i] = count
            
            return count

        
        return count_decoding(0)
        # T = O(n)
        # S = O(n), space allocated on recursive call stack
            

            

        