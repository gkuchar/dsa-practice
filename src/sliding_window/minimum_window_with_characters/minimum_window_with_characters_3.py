class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        m = len(t)
        n = len(s)

        if m > n: return ""

        tc = Counter(t)
        sc = {char:0 for char in tc.keys()}

        minn = ""
        min_len = float('inf')
        l = 0
        r = 0
        have = 0

        while r < n:
            if s[r] in tc:
                sc[s[r]] += 1
                if sc[s[r]] == tc[s[r]]:
                    have += 1
        
            while have == len(tc.keys()):
                match = s[l:r+1]
                if len(match) < min_len:
                    minn = match
                    min_len = len(match)
                
                if s[l] in tc:
                    sc[s[l]] -= 1
                    if sc[s[l]] == tc[s[l]] - 1:
                        have -= 1
                l += 1

            r += 1
            
        return minn

        # T = O(n)
        # S = O(1)