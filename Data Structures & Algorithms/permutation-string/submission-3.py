class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m: return False

        l = 0
        r = n - 1

        s1_chars = Counter(s1)
        s2_substring_chars = Counter(s2[l:r + 1])

        while r < m - 1:
            if s1_chars == s2_substring_chars: return True

            r += 1
            if s2[r] not in s2_substring_chars:
                s2_substring_chars[s2[r]] = 1
            else:
                s2_substring_chars[s2[r]] += 1
            
            s2_substring_chars[s2[l]] -= 1
            l += 1
        
        return True if s1_chars == s2_substring_chars else False

    # T = O(m)
    # S = O(26)    