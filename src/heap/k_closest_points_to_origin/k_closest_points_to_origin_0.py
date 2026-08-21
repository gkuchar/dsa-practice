import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pair in points:
            x = pair[0]
            y = pair[1]

            key = (x ** 2) + (y ** 2)

            if len(heap) < k:
                heapq.heappush(heap, (-key, pair))
                continue

            if key < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-key, pair))
        
        return [element[1] for element in heap]
        # T = O(n lg k)
        # S = O(k)