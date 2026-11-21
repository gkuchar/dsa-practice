class Solution:
    def reverseBits(self, n: int) -> int:
        val = n & 1
        n = n >> 1

        for _ in range(31):
            n_bit = n & 1
            n = n >> 1

            val = val << 1
            val = val | n_bit

        return val
        # T = O(1)
        # S = O(1)