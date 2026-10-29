class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        cache = {}

        min_coin = min(coins)
        n = len(coins)

        def add_coin(remaining, i) -> int:
            if (remaining, i) in cache:
                return cache[(remaining, i)]
            
            if remaining == 0:
                cache[(remaining, i)] = 1
                return 1
            if remaining < min_coin or i == n:
                cache[(remaining, i)] = 0
                return 0

            count = 0

            c = coins[i]
            
            use_c = add_coin(remaining - c, i)
            skip_c = add_coin(remaining, i + 1)

            count = use_c + skip_c
            cache[(remaining, i)] = count
            return count
        
        return add_coin(amount, 0)
        # T = O(a * c),  a = amount
        # S = O(a * c), c = len(coins)