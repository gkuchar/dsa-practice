class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [1, 1, 1]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: continue

            current = [max(current[0], t[0]), max(current[1], t[1]), max(current[2], t[2])]
            if current == target: return True
        
        return False
        # T = O(n)
        # S = O(1)