class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0

        longest = 1
        chars = {}

        while r < n:
            if s[r] not in chars:
                chars[s[r]] = 1
            else:
                chars[s[r]] += 1
            size = r - l + 1
            majority = max(chars.values())
            if size - majority > k:
                chars[s[l]] -= 1
                l += 1
            else:
                longest = max(longest, size)
            r += 1
        
        return longest

        # T = O(n)
        # S = O(26)
        