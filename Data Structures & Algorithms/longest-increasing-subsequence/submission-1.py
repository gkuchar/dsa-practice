class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxx = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            maxx = max(maxx, dp[i])

        return maxx
        # T = O(n^2)
        # S = O(n)
        