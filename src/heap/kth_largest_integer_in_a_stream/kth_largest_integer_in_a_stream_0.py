import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        nums = sorted(nums)
        while nums and len(self.heap) < self.k:
            num = nums.pop()
            heapq.heappush(self.heap, num)

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