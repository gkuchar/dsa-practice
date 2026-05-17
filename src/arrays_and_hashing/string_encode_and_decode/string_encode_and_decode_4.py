class Solution:
    def encode(self, strs: List[str]) -> str:
        message = ''
        for s in strs:
            size = len(s)
            prefix = f'{size}|'
            message += prefix
            message += s
        
        return message

    def decode(self, message: str) -> List[str]:
        strs = []
        n = len(message)
        i = 0
        while i < n:
            word_size = ''
            while message[i] != '|':
                word_size += message[i]
                i += 1
            word_size = int(word_size)
            word = message[i + 1 : i + 1 + word_size]
            strs.append(word)
            
            i += (1  + word_size)
        
        return strs

        # T = O(n)
        # S = O(1) - no auxiliary space used