class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        if n == 1:
            return True if triplets[0] == target else False

        sorted_by_a = sorted(triplets, key= lambda x: (x[0], x[1], x[2]))

        i = 1
        while i < n and sorted_by_a[i][0] < target[0]:
            i += 1
            if i == n: return False
        curr = sorted_by_a[i]

        while i < n and curr[0] < target[0]:
            curr = [max(curr[0], sorted_by_a[i][0]), max(curr[1], sorted_by_a[i][1]), max(curr[2], sorted_by_a[i][2])]
            if curr[0] == target[0]: break
            i += 1
        
        if i == n or curr[0] > target[0]:
            return False

        sorted_by_b = sorted(triplets, key= lambda x: (x[1], x[2]))

        i = 0
        while i < n and sorted_by_b[i][1] < target[1]:
            i += 1

        while i < n and curr[1] < target[1]:
            curr = [max(curr[0], sorted_by_b[i][0]), max(curr[1], sorted_by_b[i][1]), max(curr[2], sorted_by_b[i][2])]
            if curr[1] == target[1]: break
            i += 1

        if i == n or curr[1] > target[1] or curr[0] > target[0]:
            return False

        sorted_by_c = sorted(triplets, key= lambda x: x[2])

        i = 0
        while i < n and sorted_by_c[i][2] < target[2]:
            i += 1
        
        while i < n and curr[2] < target[2]:
            curr = [max(curr[0], sorted_by_c[i][0]), max(curr[1], sorted_by_c[i][1]), max(curr[2], sorted_by_c[i][2])]
            if curr[2] == target[2]: break
            i += 1

        if i == n or curr[2] > target[2] or curr[1] > target[1] or curr[0] > target[0]:
            return False

        return True
        # T = O(nlgn)
        # S = O(n)