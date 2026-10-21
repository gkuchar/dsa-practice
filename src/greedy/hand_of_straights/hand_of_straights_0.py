from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        counts = Counter(hand)
        sorted_keys = sorted(counts.keys())

        k = len(sorted_keys)
        key_idx = 0
        smallest = sorted_keys[key_idx]

        while n > 0:
            for i in range(groupSize):
                if smallest + i not in counts or counts[smallest + i] == 0: return False
                counts[smallest + i] -= 1
                n -= 1

            next_small = smallest
            while key_idx < k and next_small in counts and counts[next_small] == 0:
                next_small = sorted_keys[key_idx]
                key_idx += 1
            smallest = next_small
        
        return True
        # T = O(n + dlgd), d = # unique numbers in hand
        # S = O(d)
