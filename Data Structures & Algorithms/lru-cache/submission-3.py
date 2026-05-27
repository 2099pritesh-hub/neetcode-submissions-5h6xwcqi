class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        self.capacity = capacity

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            toRemove = self.left.next
            self.remove(toRemove)
            del self.cache[toRemove.key]
