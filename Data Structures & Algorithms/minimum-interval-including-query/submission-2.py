import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        sorted_intervals = sorted(intervals, key= lambda x: x[0])
        n = len(intervals)
        queries_aug = [(q, i) for i, q in enumerate(queries)]
        sorted_queries = sorted(queries_aug)
        heap = []

        i = 0
        for q, q_idx in sorted_queries:
            while i < n and sorted_intervals[i][1] < q:
                i += 1

            while i < n and q >= sorted_intervals[i][0]:
                heapq.heappush(heap, (sorted_intervals[i][1] - sorted_intervals[i][0] + 1, (sorted_intervals[i][0], sorted_intervals[i][1])))
                i += 1
            
            while heap and heap[0][1][1] < q:
                heapq.heappop(heap)
            
            res[q_idx] = heap[0][0] if heap else -1

        return res
        # T = O(nlgn + qlgq)
        # S = O(n + q)
        