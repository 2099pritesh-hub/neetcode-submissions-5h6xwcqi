class MyHashSet:

    def __init__(self):
        self.hashSet = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        for c in cur:
            if c == key:
                return
        cur.append(key)

    def remove(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        for i, c in enumerate(cur):
            if c == key:
                cur.pop(i)
                return

    def contains(self, key: int) -> bool:
        cur = self.hashSet[key % len(self.hashSet)]
        for c in cur:
            if c == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)