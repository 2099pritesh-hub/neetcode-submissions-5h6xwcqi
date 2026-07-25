class MyHashSet:

    def __init__(self):
        self.hashSet = [-1] * (10 ** 4)

    def add(self, key: int) -> None:
        self.hashSet[self.hash(key)] = key

    def remove(self, key: int) -> None:
        self.hashSet[self.hash(key)] = -1

    def contains(self, key: int) -> bool:
        if self.hashSet[self.hash(key)] != -1:
            return True
        return False

    def hash(self, key):
        return key % len(self.hashSet)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)