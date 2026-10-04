class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: x[0])
        curr_end = intervals[0][1]
        overlapping = 0

        for i, interval in enumerate(intervals):
            if i == 0:
                continue

            if interval[0] < curr_end:
                overlapping += 1
                curr_end = min(interval[1], curr_end)
            else:
                curr_end = interval[1]
        
        return overlapping
        # T = O(nlgn)
        # S = O(n)