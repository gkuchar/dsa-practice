class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        largest = nums[0]
        smallest = nums[0]
        maxx = nums[0]

        for i, num in enumerate(nums):
            if i == 0: continue

            t_large = max(num, num * smallest, num * largest)
            t_small = min(num, num * smallest, num * largest)

            largest = t_large
            smallest = t_small

            maxx = max(largest, smallest, maxx)
        
        return maxx
        # T = O(n)
        # S = O(1)
        