class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triples = []
        uniques = set()
        nums = sorted(nums)

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            goal = -nums[i]

            while l < r:
                summ = nums[l] + nums[r]
                if summ > goal:
                    r -= 1
                    continue
                if summ < goal:
                    l += 1
                    continue

                triple = [nums[i], nums[l], nums[r]]
                if tuple(sorted(triple)) not in uniques:
                    triples.append(triple)
                    uniques.add(tuple(sorted(triple)))
                
                r -= 1
                l += 1
        
        return triples

        # T = O(n^2)
        # S = O(n^2)