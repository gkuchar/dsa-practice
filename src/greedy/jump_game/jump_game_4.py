class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        max_reach = 0

        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + num)
        
        return True

        # T = O(n)
        # S = O(1)
        