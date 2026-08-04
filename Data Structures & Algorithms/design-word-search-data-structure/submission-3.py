class WordDictionary:

    # Trie as nested dicts, traverse letters and recursive search everything after '.' when encountering '.'
    def __init__(self):
        self.main = {}

    # Traverse trie, adding unseen letters as a new dict. End words with ###
    def addWord(self, word: str) -> None:
        curr_layer = self.main
        for char in word:
            if char not in curr_layer:
                curr_layer[char] = {}
            curr_layer = curr_layer[char]
        
        curr_layer['###'] = True

    # traverse trie, use letters as path and must recursive brute force search everything after '.' when encountering '.'
    def search(self, word: str) -> bool:
        return self.inner_search(word=word, curr_layer=self.main)
            
    def inner_search(self, word, curr_layer) -> bool:
        print(word)
        for i, char in enumerate(word):
            if char == '.':
                for next_char in curr_layer:
                    if next_char == '###':
                        continue
                    if self.inner_search(word=word[i+1:], curr_layer=curr_layer[next_char]):
                        return True
                return False


            if char not in curr_layer:
                print(f'curr_layer: {curr_layer}')
                print(f'missing char: {char}')
                return False

            curr_layer = curr_layer[char]
        

        return '###' in curr_layer
