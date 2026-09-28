class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        most_neg = nums[0]
        most_pos = nums[0]
        maxx = nums[0]

        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            t_neg = min(num * most_neg, num * most_pos, num)
            t_pos = max(num * most_neg, num * most_pos, num)

            most_neg = t_neg
            most_pos = t_pos

            maxx = max(maxx, most_pos)
        
        return maxx
        # T = O(n)
        # S = O(1)

        