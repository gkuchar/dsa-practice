class LRUCache:

    # S = O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = []
        

    # T = O(n)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            if len(self.lru) > self.capacity:
                self.lru = self.lru[1:]
            return self.cache[key]
        else:
            return -1
        
    # T = O(n)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
            return
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.lru.append(key)
            return
        
        while len(self.lru) >= self.capacity:
            self.cache.pop(self.lru[0], None)
            self.lru = self.lru[1:]

        self.cache[key] = value
        self.lru.append(key)
        return


