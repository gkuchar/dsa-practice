class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        zero = False
        summ, maxx = 0, 0
        for num in nums:
            if num == 0: zero = True
            if num > maxx:
                maxx = num
    
        for i in range(maxx + 1):
            summ += i
    
        for num in nums:
            summ -= num
        
        return maxx + 1 if summ == 0 and zero else summ
        # T = O(n)
        # S = O(1)
