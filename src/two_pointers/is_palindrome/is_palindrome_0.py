class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        letters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


        while l < r:
            if s[l] not in nums and s[l].lower() not in letters:
                l += 1
                continue
            if s[r] not in nums and s[r].lower() not in letters:
                r -= 1
                continue

            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        
        return True

        # T = O(n)
        # S = O(1)
        