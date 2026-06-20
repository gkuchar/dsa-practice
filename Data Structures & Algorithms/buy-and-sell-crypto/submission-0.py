class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        n = len(prices)

        for i in range(n):
            lowest = min(lowest, prices[i])
            profit = prices[i] - lowest
            max_profit = max(max_profit, profit)

        return max_profit
        
        # T = O(n)
        # S = O(1)