class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        smapp = {}

        for char in s:
            if char not in smapp:
                smapp[char] = 1
            else:
                smapp[char] += 1
        
        for char in t:
            if char not in smapp: return False
            if smapp[char] == 0: return False
            smapp[char] -= 1

        for count in smapp.values():
            if count != 0: return False

        return True 