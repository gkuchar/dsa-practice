class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx, curr = nums[0], nums[0]

        for i, num in enumerate(nums):
            if i == 0: continue
            
            if curr < 0:
                curr = 0
            
            curr += num
            maxx = max(maxx, curr)
        
        return max(maxx, curr)
        # T = O(n)
        # S = O(1)
        
        