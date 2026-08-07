class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack_dfs(path, h):
            nonlocal nums
            
            # complete answer when append choice is made on all elements in nums
            if h == len(nums):
                result.append(path[:])
                return
            
            # choice 1: append current int
            path.append(nums[h])
            backtrack_dfs(path, h + 1)
            path.pop()

            # choice 2: do not append current int
            backtrack_dfs(path, h + 1)

        backtrack_dfs([], 0)
        return result

    # T = O(n * 2^n), linear factor from copy, exponential factor from binary recursion structure
    # S = O(n * 2^n), output holds 2^n lists, with each list holding up to n ints