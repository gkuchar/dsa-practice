class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m: return False

        s1_chars = Counter(s1)

        for i, char in enumerate(s2):
            if char not in s1_chars: continue
            s2_substring = s2[i:i + n]
            #print(f's2_substring: {s2_substring}')
            #print(f's1: {s1}')
            s2_substring_chars = Counter(s2_substring)
            #print(f's2: {s2_substring_chars}')
            #print(f's1: {s1_chars}')
            if s1_chars == s2_substring_chars: return True
        
        return False

        