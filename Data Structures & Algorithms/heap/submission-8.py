class MinHeap:
    
    def __init__(self):
        self.minHeap = [0]

    def push(self, val: int) -> None:
        self.minHeap.append(val)
        i = len(self.minHeap) - 1

        while i > 1 and self.minHeap[i // 2] > self.minHeap[i]:
            self.minHeap[i // 2], self.minHeap[i] = self.minHeap[i], self.minHeap[i // 2]
            i = i // 2

    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        if len(self.minHeap) == 2:
            return self.minHeap.pop()
        
        res = self.minHeap[1]
        self.minHeap[1] = self.minHeap.pop()
        i = 1
        self.percolateDown(i)
        return res    
        
    def top(self) -> int:
        return self.minHeap[1] if len(self.minHeap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.minHeap = [0] + nums

        cur = (len(self.minHeap) - 1) // 2
        while cur > 0:
            i = cur
            self.percolateDown(i)
            cur -= 1
    
    def percolateDown(self, i):
        while 2 * i < len(self.minHeap):
            if (2 * i + 1 < len(self.minHeap) and
                self.minHeap[2 * i + 1] < self.minHeap[2 * i] and
                self.minHeap[i] > self.minHeap[2 * i + 1]):
                self.minHeap[i], self.minHeap[2 * i + 1] = self.minHeap[2 * i + 1], self.minHeap[i]
                i = 2 * i + 1
            elif self.minHeap[i] > self.minHeap[2 * i]:
                self.minHeap[i], self.minHeap[2 * i] = self.minHeap[2 * i], self.minHeap[i]
                i = 2 * i
            else:
                break