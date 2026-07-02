class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = ListNode(0), ListNode(0)
        self.left.next, self.right.prev = self.right, self.left 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val[1] = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = ListNode([key, value])
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            toEvict = self.left.next
            self.remove(toEvict)
            del self.cache[toEvict.val[0]]        
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = self.right.prev = node