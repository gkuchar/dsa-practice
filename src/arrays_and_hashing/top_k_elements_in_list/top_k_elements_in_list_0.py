class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        ret = []

        for num in nums:
            if num not in counts:
                counts[num] = -1
            else:
                counts[num] -= 1
        
        heap = [(v, k) for k, v in counts.items()]
        heapq.heapify(heap)

        for i in range(k):
            v, k = heapq.heappop(heap)
            ret.append(k)
        
        return ret
    
        # T = O(n)
        # S = O(n)