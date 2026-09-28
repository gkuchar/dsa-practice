class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def first_word(sub_s):
            if sub_s in cache:
                return cache[sub_s]
            
            for word in wordDict:

                if word == sub_s:
                    cache[sub_s] = True
                    return True

                n = len(word)
                if sub_s[:n] == word:
                    if first_word(sub_s[n:]):
                        cache[sub_s[n:]] = True
                        return True
            
            cache[sub_s] = False
            return False


        return first_word(s)
        # T = O(n * m * t), n = len(s), m = len(wordDict), t = max len of word in wordDict
        # S = O(n^2)