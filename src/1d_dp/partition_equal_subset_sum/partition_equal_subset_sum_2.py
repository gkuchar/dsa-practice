class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        n = len(nums)
        target = total // 2

        cache = {}
        
        def search_subset(i, curr_sum):
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            
            if curr_sum == target:
                return True
            
            if i >= n:
                return False
            
            not_include = search_subset(i + 1, curr_sum)
            if not_include:
                return True
            else:
                cache[(i + 1, curr_sum)] = False

            include = search_subset(i + 1, curr_sum + nums[i])
            if include:
                return True
            else:
                cache[(i + 1, curr_sum + nums[i])] = False

            return False

        return search_subset(0, 0)
        # T = O(n * t), n = len(arr), t = target
        # S = O(n * t)

