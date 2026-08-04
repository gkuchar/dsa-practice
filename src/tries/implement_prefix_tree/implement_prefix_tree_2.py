class PrefixTree:

    # Nested dicts with chars as keys
    # S = O(m), m = sum of chars in all words
    def __init__(self):
        self.main = {}

    # traverse the tree of dicts, creating the path with the new char if it doesnt currently exist.
    # ### marks end of work
    def insert(self, word: str) -> None:
        curr_layer = self.main
        for char in word:
            if char not in curr_layer:
                curr_layer[char] = {}
            curr_layer = curr_layer[char]
        curr_layer['###'] = True
    # T = O(n), n = len(word)
        
    # traverse tree of dicts, if reach end and there is no chars after (i.e. ### in dict), then return True
    def search(self, word: str) -> bool:
        print(f'search {word}')
        curr_layer = self.main
        for char in word:
            if char not in curr_layer: return False
            curr_layer = curr_layer[char]
        return '###' in curr_layer
    # T = O(n), n = len(word)

    # traverse tree of dicts, if reach end of prefix then return True
    def startsWith(self, prefix: str) -> bool:
        curr_layer = self.main
        for char in prefix:
            if char not in curr_layer: return False
            curr_layer = curr_layer[char]
        
        return True
    # T = O(n), n = len(prefix)
    