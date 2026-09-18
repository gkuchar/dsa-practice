class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triples = []
        nums = sorted(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

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
                triples.append(triple)
                
                r -= 1
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
        
        return triples

        # T = O(n^2)
        # S = O(1)