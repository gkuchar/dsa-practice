class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[-1, -1] for _ in range(n)]

        def advance(i, coin_held) -> int:
            if i >= n:
                return 0
            
            if coin_held and cache[i][1] >= 0:
                return cache[i][1]
            
            if not coin_held and cache[i][0] >= 0:
                return cache[i][0]

            if coin_held:
                best_no_coin = advance(i + 2, False) + prices[i]
                best_coin = advance(i + 1, True)

                cache[i][1] = max(best_coin, best_no_coin)
                return cache[i][1]
            else:
                best_no_coin = advance(i + 1, False) 
                best_coin = advance(i + 1, True) - prices[i]

                cache[i][0] = max(best_no_coin, best_coin)
                return cache[i][0]

        advance(0, False)
        return cache[0][0]

        # T = O(n)
        # S = O(n)