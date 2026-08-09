class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def dfs_bt(path, i):
            if i == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[i])
            dfs_bt(path, i + 1)
            path.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs_bt(path, i + 1)

        
        dfs_bt([], 0)

        return result