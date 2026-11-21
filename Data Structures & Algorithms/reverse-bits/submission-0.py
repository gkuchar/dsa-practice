class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        n_str = str(bin(n))[2:]
        padding = 32 - len(n_str)

        for i, bit in enumerate(n_str):
            if bit == '1':
                power = 2**(i + padding)
                val += power
        
        return val
        # T = O(1)
        # S = O(1)