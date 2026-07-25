class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(-1) for _ in range(10000)]

    def add(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            cur = cur.next
            if cur.key == key:
                return
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                break
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            cur = cur.next
            if cur.key == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)