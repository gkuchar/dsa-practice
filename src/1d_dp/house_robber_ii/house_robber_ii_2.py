class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        def linear_max_money(arr, name):
            print(arr)
            m = len(arr)
            dp = [0] * m
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, m):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

            print(name, dp)
            return dp[m - 1]
        
        front = linear_max_money(nums[:n - 1], 'front')
        print(f'front: {front}')
        back = linear_max_money(nums[1:], 'back')
        print(f'back: {back}')
        return max(front, back)