class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        nums[n - 1] = n - 1
        for i in range(n-2, -1, -1):
            max_jump = nums[i]
            furthest_idx = i
            for j in range(1, max_jump + 1):
                furthest_idx = max(nums[min(i + j, n - 1)], furthest_idx)
            
            nums[i] = furthest_idx
        
        return nums[0] == n - 1
        # T = O(n)
        # S = O(1)
        