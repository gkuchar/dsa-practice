class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return jumps + 1
            
            if i == curr_end:
                curr_end = farthest
                jumps += 1
        
        # T = O(n)
        # S = O(1)