class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = 0

        for i in range(n + 1):
            missing = missing ^ i
            if i < n:
                missing = missing ^ nums[i]
        
        return missing

        # T = O(n)
        # S = O(1)