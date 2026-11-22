class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
    
        for i in range(n + 1):
            summ += i
    
        for num in nums:
            summ -= num
        
        return summ
        # T = O(n)
        # S = O(1)