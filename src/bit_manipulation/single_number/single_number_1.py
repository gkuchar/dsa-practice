class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = nums[0]

        for i in range(1, len(nums)):
            bits = bits ^ nums[i]

        return bits
        # T = O(n)
        # S = O(1)