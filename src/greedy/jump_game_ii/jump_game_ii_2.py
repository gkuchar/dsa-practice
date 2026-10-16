class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        nums[-1] = 0

        for i in range(n - 2, -1, -1):
            max_jump = nums[i]
            min_jumps = float('inf')
            for j in range(1, max_jump + 1):
                if i + j < n and nums[i + j] < min_jumps:
                    min_jumps = nums[i + j] + 1
            
            nums[i] = min_jumps
        
        return nums[0]
        # T = O(n^2)
        # S = O(1)