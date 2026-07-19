class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        prev = None
        while True:
            if nums[i] == 0:
                return prev + 1
            prev = nums[i] - 1
            t = i
            i = nums[i]
            nums[t] = 0
        