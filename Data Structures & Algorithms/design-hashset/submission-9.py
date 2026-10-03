class MyHashSet:

    def __init__(self):
        self.hashSet = [[]] * 10000

    def add(self, key: int) -> None:
        index = key % 10000
        bucket = self.hashSet[index]
        for k in bucket:
            if k == key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        index = key % 10000
        bucket = self.hashSet[index]
        for k in bucket:
            if k == key:
                bucket.remove(k)
                return

    def contains(self, key: int) -> bool:
        index = key % 10000
        bucket = self.hashSet[index]
        for k in bucket:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)