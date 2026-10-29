class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        cache = {}

        min_coin = min(coins)
        n = len(coins)

        def add_coin(remaining, i) -> int:
            if (remaining, i) in cache:
                return cache[(remaining, i)]
            
            if remaining < min_coin:
                cache[(remaining, i)] = 0
                return 0

            count = 0
            for j in range(i, n):
                c = coins[j]
                if remaining == c:
                    count += 1
                if remaining > c:
                    count += add_coin(remaining - c, j)
            
            cache[(remaining, i)] = count
            return count
        
        return add_coin(amount, 0)
        # T = O(a * c^2),  a = amount
        # S = O(a * c), c = len(coins)