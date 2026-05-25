class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1
        max_area = 0

        def get_area(l: int, r: int) -> int:
            height = min(heights[l], heights[r])
            width = r - l

            return height * width

        while l < r:
            max_area = max(max_area, get_area(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

    # T = O(n)
    # S = O(1)