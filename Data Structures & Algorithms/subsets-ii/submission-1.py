class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def dfs_bt(path, i):
            result.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                path.append(nums[j])
                dfs_bt(path, j + 1)
                path.pop()

        
        dfs_bt([], 0)

        return result

        