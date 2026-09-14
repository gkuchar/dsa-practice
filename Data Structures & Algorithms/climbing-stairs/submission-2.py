class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        # intuition: can get to step n from either n - 1 (by taking 1 step), or n - 2 (taking 2 steps)
        # Thus, the amount of ways to reach step n is the amount of ways reaching n - 1 + ways of reaching n - 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]
        # T = O(n)
        # S = O(n)