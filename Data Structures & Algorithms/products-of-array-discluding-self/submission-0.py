class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        postfix = [0 for _ in range(n)]

        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(n):
            prefix[i] *= postfix[i]
        
        return prefix

        # T = O(n)
        # S = O(n)