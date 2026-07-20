class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = None


class LRUCache:

    # S = O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_head = None
        self.lru_tail = None
        self.cache = {}

    # T = O(1)
    def move_to_tail(self, node):
        if node is self.lru_tail:
            return

        if node is self.lru_head:
            self.lru_head = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.lru_tail
        self.lru_tail.next = node
        node.next = None

        self.lru_tail = node
        
    # T = O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_tail(node)

        return node.val

    # T = O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_tail(node)
            return
    
        if len(self.cache) == self.capacity:
            old_head = self.lru_head
            if self.capacity == 1:
                self.lru_head = None
                self.lru_tail = None
            else:
                self.lru_head = self.lru_head.next
                self.lru_head.prev = None

            self.cache.pop(old_head.key)
        
        new_node = Node(val=value)
        new_node.key = key

        if len(self.cache) == 0:
            self.cache[key] = new_node
            self.lru_head = new_node
            self.lru_tail = new_node
            new_node.prev = None
            return

        self.cache[key] = new_node
        new_node.prev = self.lru_tail
        self.lru_tail.next = new_node
        self.lru_tail = new_node
        return
    

        
