class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # append + merge algortithm: t= O(nlng), s = O(n)
        # targetted insert: t = O(n), s= O(n)

        merged = []
        n = len(intervals)
        i = 0
        while i < n and newInterval[0] > intervals[i][1]:
            merged.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1
        
        return merged
        # T = O(n)
        # S = O(n)