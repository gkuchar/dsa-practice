class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for char in s:
            if char in mapp:
                stack.append(char)
            else:
                if not stack or mapp[stack.pop()] != char:
                    return False

        return not bool(stack)

        # T = O(n)
        # S = O(n)        