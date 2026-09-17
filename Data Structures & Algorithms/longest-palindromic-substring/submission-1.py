class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = s[0]

        for i in range(1, n - 1):
            j = 1
            while i - j > -1 and i + j < n and s[i - j] == s[i + j]:
                j += 1
            
            j -= 1
            if j * 2 + 1 > len(longest):
                longest = s[i - j: i + j + 1]     

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                l = 1
                r = 2
                while i - l > -1 and i + r < n and s[i - l] == s[i + r]:
                    l += 1
                    r += 1

                l -= 1
                r -= 1
                if l * 2 + 2 > len(longest):
                    longest = s[i - l:i + r + 1]
                
        return longest
        # T = O(n^2)
        # S = O(1)