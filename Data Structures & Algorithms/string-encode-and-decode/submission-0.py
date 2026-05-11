class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            encoded = ''
            n = len(s)
            if n == 0:
                ret += '#'
                continue
            c = 1
            curr = s[0]
            i = 1
            while i < n:
                if s[i] == curr:
                    c += 1
                else:
                    encoded += str(c)
                    encoded += curr
                    curr = s[i]
                    c = 1
                i += 1
            
            encoded += str(c)
            encoded += curr
            ret += encoded
            ret += '#'
                
        return ret
        # T = O(n), S = O(n)
    
    def decode(self, s: str) -> List[str]:
        words = []
        n = len(s)
        word = ''
        i = 0
        while i < n:
            if s[i] == '#':
                words.append(word)
                word = ''
                i += 1
            else:
                num = int(s[i])
                char = s[i + 1]
                word += char * num
                i += 2
        
        return words
        # T = O(n), S = O(n)





