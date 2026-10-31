class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3): return False

        memo = {}
        
        def interleave(i, j, k, prev) -> bool:
            if (i, j, prev) in memo:
                return memo[(i, j, prev)]

            if k >= len(s3):
                memo[(i, j, prev)] = True
                return True
            
            if prev != 1:
                for end in range(i, n):
                    sub = s1[i:end + 1]
                    length = end + 1 - i
                    if s3[k:k + length] == sub:
                        interleaved = interleave(i + length, j, k + length, 1)
                        if interleaved:
                            memo[(i, j, prev)] = True
                            return True
                    else:
                        memo[(i, j, prev)] = False
                        return False       
            else:
                for end in range(j, m):
                    sub = s2[j:end + 1]
                    length = end + 1 - j
                    if s3[k:k + length] == sub:
                        interleaved = interleave(i, j + length, k + length, 2)
                        if interleaved:
                            memo[(i, j, prev)] = True
                            return True
                    else:
                        memo[(i, j, prev)] = False
                        return False 
            
            memo[(i, j, prev)] = False
            return False

        return interleave(0, 0, 0, 2) or  interleave(0, 0, 0, 1)
        # T = O(n * m)
        # S = O(n * m)