class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates) # sort to skip duplicates on the same sibling level

        def dfs_backtrack(path, path_sum, start, candidates, target):
            nonlocal result

            # complete solution if sum equals target
            if path_sum == target:
                result.append(path[:])
                return
            
            # no negative numbers, so overshooting sum guarantees target could not be hit
            if path_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # dont want to repeat the same path on a int we have already seen in the same layer
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs_backtrack(path, path_sum + candidates[i], i + 1, candidates, target)
                path.pop()
        
        dfs_backtrack([], 0, 0, candidates, target)
        return result

        # T = O(n * 2^n), linear factor from copy, exponential factor from include/not include at each node
        # Total S = O(n^2)
        # Auxiliary S = O(n^2), set  at worst akes up n + n - 1 + ... + 1 -> n(n+1) / 2 -> n^2