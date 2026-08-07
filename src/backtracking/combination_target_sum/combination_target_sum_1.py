class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack_dfs(path, path_sum, start, nums, target):
            nonlocal result

            # complete solution if sum equals target
            if path_sum == target:
                result.append(path[:])
                return
            
            # no negative numbers, so overshooting sum guarantees target could not be hit
            if path_sum > target:
                return
            
            # explore path for each number ahead of the current number (including current)
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack_dfs(path, path_sum + nums[i], i, nums, target)
                path.pop()

        backtrack_dfs([], 0, 0, nums, target)

        return result
        # t = target, m = min(nums), k = t/m, n = len(nums)
        # T = O(k * n^k), linear factor from copy, n^k factor from exploring n paths with longest path being k long
        # Total S = O(k * n^k), Auxiliary S = O(k)