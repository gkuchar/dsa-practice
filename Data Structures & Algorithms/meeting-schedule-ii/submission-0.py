"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n < 2:
            return n
        
        rooms_needed = 1
        sorted_intervals = sorted(intervals, key= lambda x: x.start)
        heap = [(sorted_intervals[0].end, sorted_intervals[0].start)]

        for i in range(1, n):
            interval = sorted_intervals[i]
            if interval.start < heap[0][0]:
                heapq.heappush(heap, (interval.end, interval.start))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, (interval.end, interval.start))
            
            rooms_needed = max(rooms_needed, len(heap))
        
        return rooms_needed
        # T = O(nlgn)
        # S = O(n)