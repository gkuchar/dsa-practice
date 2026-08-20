import heapq
class KthLargest:

    # T = O(nlgn)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # T = O(lgk)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val <= self.heap[0]:
            return self.heap[0]
        else:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]

# S = O(k)