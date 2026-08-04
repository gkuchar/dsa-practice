class WordDictionary:

    # Trie as nested dicts, traverse letters and recursive brute force search everything after '.' when encountering '.'
    def __init__(self):
        self.main = {}
    # S = O(m), m = sum of all chars in words

    # Traverse trie, adding unseen letters as a new dict. End words with ###
    def addWord(self, word: str) -> None:
        curr_layer = self.main
        for char in word:
            if char not in curr_layer:
                curr_layer[char] = {}
            curr_layer = curr_layer[char]
        
        curr_layer['###'] = True
    # T = O(n), n = len(word)

    # traverse trie, use letters as path and must recursive brute force search everything after '.' when encountering '.'
    def search(self, word: str) -> bool:
        return self.inner_search(word=word, curr_layer=self.main)
            
    def inner_search(self, word, curr_layer) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                for next_char in curr_layer:
                    if next_char == '###':
                        continue
                    if self.inner_search(word=word[i+1:], curr_layer=curr_layer[next_char]):
                        return True
                return False


            if char not in curr_layer:
                return False

            curr_layer = curr_layer[char]
    
        return '###' in curr_layer
        # T = O(n * 26^d), n = len(word), d = # .
