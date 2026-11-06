class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        padded = [1] + nums + [1]

        def get_coins(left, right):
            if right == left + 1:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            max_coins = 0

            for k in range(left + 1, right):
                max_left = get_coins(left, k)
                max_right = get_coins(k, right)

                popped = padded[left] * padded[k] * padded[right]

                coins = popped + max_left + max_right

                max_coins = max(max_coins, coins)
            
            memo[(left, right)] = max_coins
            return max_coins
        
        return get_coins(0, n + 1)
        # T = O(n^3)
        # S = O(n^2)