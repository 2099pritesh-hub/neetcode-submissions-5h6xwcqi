class ListNode:
    
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt

    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        node.next, node.prev = nxt, prev
        nxt.prev = prev.next = node