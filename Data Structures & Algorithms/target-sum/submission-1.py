class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = {}

        def ways_from_curr(i, summ):
            if (i, summ) in memo:
                return memo[(i, summ)]

            if i == n:
                value = 1 if summ == target else 0
                memo[(i, summ)] = value
                return value

            ways_add = ways_from_curr(i + 1, summ + nums[i])

            ways_sub = ways_from_curr(i + 1, summ - nums[i])

            memo[(i, summ)] = ways_add + ways_sub
            return ways_add + ways_sub
        
        return ways_from_curr(0, 0)
        # T = O(n * s), n = len(nums), s = number of distinct sums
        # S = O(n * s)