class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        n_minus_2 = 1
        n_minus_1 = 2

        # intuition: can get to step n from either n - 1 (by taking 1 step), or n - 2 (taking 2 steps)
        # Thus, the amount of ways to reach step n is the amount of ways reaching n - 1 + ways of reaching n - 2
        for _ in range(2, n):
            t = n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = t + n_minus_1
        
        return n_minus_1
        # T = O(n)
        # S = O(1)