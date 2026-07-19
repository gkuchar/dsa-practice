class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        fast = 0

        # Use floyd's fast/slow cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Beginning of cycle is the element that is the same distance from index 0
        # and where slow/fast intersected. Beginning of cycle is a duplicate element
        curr = 0
        while True:
            curr = nums[curr]
            slow = nums[slow]

            if curr == slow: return curr
        
        # T = O(n)
        # S = O(1), no modifications to nums