"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key= lambda x: x.start)

        for i, interval in enumerate(sorted_intervals):
            if i == 0: continue

            if interval.start < sorted_intervals[i - 1].end:
                return False
        
        return True
        # T = O(nlgn)
        # S = O(n)