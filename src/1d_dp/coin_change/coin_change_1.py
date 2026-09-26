class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)

        if amount == 0: return 0
        dp = [-1] * (amount + 1)

        for a in range(1, amount + 1):
            if a in coins_set:
                dp[a] = 1
                continue
            
            remaining_min = 10001
            for coin in coins:
                remaining = a - coin
                if remaining < 0:
                    continue
                remaining_can = dp[remaining]
                remaining_min = min(remaining_min, remaining_can)

            dp[a] = remaining_min + 1
        
        return dp[amount] if dp[amount] != 10002 else -1
        # T = O(c * n), c = # coins, n = amount
        # S = O(c + n)