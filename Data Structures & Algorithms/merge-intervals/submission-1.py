class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        sorted_intervals = sorted(intervals, key= lambda x: x[0])

        for interval in sorted_intervals:
            start, end = interval[0], interval[1]
            if not merged or start > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(end, merged[-1][1])

        
        return merged
        # T = O(nlgn)
        # S = O(n)