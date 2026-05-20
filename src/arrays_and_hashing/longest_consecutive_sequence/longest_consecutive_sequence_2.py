class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set: continue
            count = 1
            while num + 1 in nums_set:
                count += 1
                num += 1
            longest = max(longest, count)
        
        return longest

        # T = O(n)
        # S = O(n)