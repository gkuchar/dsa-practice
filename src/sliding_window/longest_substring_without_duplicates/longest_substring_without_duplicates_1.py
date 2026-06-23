class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        l = 0
        r = 1
        longest = 1

        curr = set()
        curr.add(s[0])

        while r < n:
            if s[r] in curr:
                longest = max(longest, len(curr))
                while s[l] != s[r]:
                    curr.remove(s[l])
                    l += 1
                curr.remove(s[l])
                l += 1
                continue
            curr.add(s[r])
            r += 1

        return max(longest, len(curr))
    
    # T = O(n)
    # S = O(n)