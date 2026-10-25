class Solution:
    def checkValidString(self, s: str) -> bool:
        start, end = 0, 0

        for char in s:
            if char == '(':
                start += 1
                end += 1
            elif char == '*':
                start = max(0, start - 1)
                end += 1
            else:
                start = max(0, start - 1)
                end -= 1
            
            if end < 0:
                return False
        
        return False if start > 0 else True
        # T = O(n)
        # S = O(1)