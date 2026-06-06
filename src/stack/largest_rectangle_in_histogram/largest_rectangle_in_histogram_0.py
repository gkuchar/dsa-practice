class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = heights[0]

        for i in range(n):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                continue
            
            while stack and heights[i] < heights[stack[-1]]:
                h_i = stack.pop()
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                right = i - 1
                area = heights[h_i] * (right - left + 1)
                max_area = max(max_area, area)
            stack.append(i)

        while stack:
            h_i = stack.pop()
            if stack:
                left = stack[-1] + 1
            else:
                left = 0
            right = n - 1
            area = heights[h_i] * (right - left + 1)
            max_area = max(max_area, area)
        
        return max_area

        # T = O(n)
        # S = O(n)