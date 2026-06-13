class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        lower = 1
        upper = max(piles)
        min_k = upper
        min_ttf = upper * n

        while lower <= upper:
            k = (lower + upper) // 2
            ttf = 0
            for pile in piles:
                ttf += math.ceil(pile / k)
            if ttf <= h and k < min_k:
                min_ttf = ttf
                min_k = k
                upper = k - 1
            else:
                lower = k + 1
            
        return min_k

        # T = O(n * lg(m)): n = len(piles), m = max(piles)
        # S = O(1)