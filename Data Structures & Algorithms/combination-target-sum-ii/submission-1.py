class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)

        def dfs_backtrack(path, path_sum, start, candidates, target):
            nonlocal result

            if path_sum == target:
                result.append(path[:])
                return
            
            if path_sum > target:
                return
            
            seen = set()
            for i in range(start, len(candidates)):
                if candidates[i] not in seen:
                    path.append(candidates[i])
                    dfs_backtrack(path, path_sum + candidates[i], i + 1, candidates, target)
                    path.pop()
                    seen.add(candidates[i])
        
        dfs_backtrack([], 0, 0, candidates, target)
        return result

        # T = O(n * 2^n), linear factor from copy, exponential factor from include/not include at each node
        # Total S = O(n^2)
        # Auxiliary S = O(n^2), set  at worst akes up n + n - 1 + ... + 1 -> n(n+1) / 2 -> n^2