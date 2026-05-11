class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        seen = set()

        for num in nums:
            seen.add(num)
        
        for num in nums:
            if num - 1 not in seen:
                length = 1
                while num + 1 in seen:
                    length += 1
                    num += 1
                longest = max(length, longest)
                
        return longest  
        