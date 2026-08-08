class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs_bt(path, seen):

            # complete solution when all nums have been added to the current permutation
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # continue down using numbers not in the current incomplete permutation
            for num in nums:
                if num not in seen:
                    path.append(num)
                    seen.add(num) # prevent current number from being reused in same permutation
                    dfs_bt(path, seen) # dfs
                    path.pop() # backtrack
                    seen.remove(num) # allow current number to be used in sibling permutations
        
        dfs_bt([], set())
        return result
    # T = O(n * n!), starting with each number in nums, completing the permutation take n!
    # Auxiliary S = O(n), seen set
    # Total S = O(n * n!)

        