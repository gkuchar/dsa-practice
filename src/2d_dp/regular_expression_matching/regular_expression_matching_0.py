class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        memo = {}

        def char_match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                return True if i == n else False
            
            first_match = i < n and (s[i] == p[j] or p[j] == '.')
            if j + 1 < m and p[j + 1] == '*': # dont use char* advances pattern, use char* advances string by 1
                one_more_match = char_match(i + 1, j) if first_match else False

                ret = char_match(i , j + 2) or one_more_match
                memo[(i, j)] = ret
                return ret
            elif first_match: # match char or single wildcard advanced both (string and pattern) by 1
                ret = char_match(i + 1, j + 1) 
                memo[(i, j)] = ret
                return ret
            else:
                ret = False
                memo[(i, j)] = ret
                return ret # dead end

        return char_match(0, 0)
        # T = O(n * m)
        # S = O(n * m)