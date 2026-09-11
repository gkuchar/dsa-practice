import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
    
        def are_valid_indices(x, y):
            return x > -1 and x < n and y > -1 and y < n

        seen.add((0, 0))
        heap = [(grid[0][0], 0, 0)]
        while heap:
            max_d, i, j = heapq.heappop(heap)

            if i == n - 1 and j == n - 1:
                return max_d
            
            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if are_valid_indices(x, y) and (x, y) not in seen:
                    new_max_d = max(max_d, grid[x][y])
                    heapq.heappush(heap, (new_max_d, x, y))
                    seen.add((x, y))
        
        # T = O(n^2 lgn)
        # S = O(n^2)

        