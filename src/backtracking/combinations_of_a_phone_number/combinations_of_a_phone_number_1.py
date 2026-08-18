class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letters = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        result = []
        def dfs_bt(path, i):
            nonlocal result
            nonlocal digits

            if len(path) == len(digits):
                result.append(''.join(path))
                return
            
            digit = digits[i]
            for letter in letters[digit]:
                path.append(letter)
                dfs_bt(path, i + 1)
                path.pop()
        
        dfs_bt([], 0)

        return result
        # T = O(n * 4^n), n = len(digits)
        # auxilary S = O(n), from builiding path / space allocated on recursive call stack
        # total S = O(n * 4^n), result holdsn 4^n strings of length n
        