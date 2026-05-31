class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        if n == 1: return [0]

        stack = []
        result = [0] * n

        for i in range(n):
            if not stack or temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    temp, idx = stack.pop()
                    result[idx] = i - idx
                stack.append((temperatures[i], i))

        return result

        # T = O(n)
        # S = O(n)