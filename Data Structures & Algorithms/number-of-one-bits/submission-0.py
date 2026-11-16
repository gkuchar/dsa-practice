class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0

        while n > 0:
            ones += n & 1
            n = n >> 1
        
        return ones
        # T = O(32)
        # S = O(1)