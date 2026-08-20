import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)

            if x == y:
                continue
            
            res = abs(x - y)
            heapq.heappush(max_heap, -res)
        
        if max_heap:
            return  -1 * max_heap[0]
        else:
            return 0
    
    # T = O(n * lgn)
    # S = O(n)