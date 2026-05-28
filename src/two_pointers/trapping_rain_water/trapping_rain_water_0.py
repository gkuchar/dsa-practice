class Solution:
    def trap(self, height: List[int]) -> int:
        summ = 0
        n = len(height)
        l = 0
        r = n - 1
        max_l = (l, height[l])
        max_r = [0] * n

        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i + 1])

        for i in range(1, n - 1):
            while l < i:
                if height[l] > max_l[1]:
                    max_l = (l, height[l])
                l += 1
            
            h_i = min(max_r[i], max_l[1]) - height[i]

            summ += max(0, h_i)
        
        return summ
                
        # T = O(n)
        # S = O(n)
        