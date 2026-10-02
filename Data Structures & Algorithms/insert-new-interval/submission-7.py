class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # append + merge algortithm: t= O(nlng), s = O(n)
        # targetted insert: t = O(n), s= O(1)

        n = len(intervals)
        if n == 0: return [newInterval]

        new_start, new_end = newInterval[0], newInterval[1]

        left = -1
        right = n
        for i in range(n):
            start, end = intervals[i][0], intervals[i][1]
            if new_start < start or (new_start == start and new_end <= end):
                left = i - 1
                right = i
                break
            left = n - 1

        if left == -1:
            intervals.insert(0, [new_start, new_end])
            left = 0
            right += 1
        elif (new_start <= intervals[left][1]):
            intervals[left][1] = max(new_end, intervals[left][1])
        else:
            intervals.insert(left + 1, [new_start, new_end])
            left += 1
            right += 1

        while right < len(intervals) and intervals[right][0] <= intervals[left][1]:
            intervals[left][1] = max(intervals[left][1], intervals[right][1])
            right += 1

        del intervals[left + 1:right]

        return intervals
        # T = O(n)
        # S = O(1)
            