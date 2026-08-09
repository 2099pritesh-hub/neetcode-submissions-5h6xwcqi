class ListNode:

    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode() for _ in range(10 ** 4)]

    def add(self, key: int) -> None:
        index = self.hashing(key)
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                return None
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hashing(key)
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return None
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = self.hashing(key)
        cur = self.hashSet[index]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False

    def hashing(self, key: int) -> int:
        return key % len(self.hashSet)        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)