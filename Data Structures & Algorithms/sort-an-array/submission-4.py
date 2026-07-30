class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.maxHeap = []
        self.heapify(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i] = self.pop()
        return nums

    def heapify(self, arr):
        self.maxHeap = [0] + arr
        cur = (len(self.maxHeap) - 1) // 2

        while cur > 0:
            i = cur
            self.percolateDown(i)
            cur -= 1
    
    def pop(self):
        if len(self.maxHeap) == 2:
            return self.maxHeap.pop()
        
        res = self.maxHeap[1]
        self.maxHeap[1] = self.maxHeap.pop()
        i = 1
        self.percolateDown(i)
        return res

    def percolateDown(self, i):
        while 2 * i < len(self.maxHeap):
            if (2 * i + 1 < len(self.maxHeap) and
                self.maxHeap[2 * i + 1] > self.maxHeap[2 * i] and
                self.maxHeap[i] < self.maxHeap[2 * i + 1]):
                self.maxHeap[i], self.maxHeap[2 * i + 1] = self.maxHeap[2 * i + 1], self.maxHeap[i]
                i = 2 * i + 1
            elif self.maxHeap[i] < self.maxHeap[2 * i]:
                self.maxHeap[i], self.maxHeap[2 * i] = self.maxHeap[2 * i], self.maxHeap[i]
                i = 2 * i
            else:
                break