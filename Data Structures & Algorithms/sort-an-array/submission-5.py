class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = [0] + nums
        self.maxHeapLen = len(self.nums)
        self.heapify(self.nums)
        for i in range(len(self.nums) - 1, 1, -1):
            self.pop()
        return self.nums[1:]

    def heapify(self, arr):
        cur = (self.maxHeapLen - 1) // 2

        while cur > 0:
            i = cur
            self.percolateDown(i)
            cur -= 1
    
    def pop(self):
        if self.maxHeapLen == 2:
            return self.nums.pop()
        
        self.maxHeapLen -= 1
        self.nums[1], self.nums[self.maxHeapLen] = self.nums[self.maxHeapLen], self.nums[1]
        i = 1
        self.percolateDown(i)

    def percolateDown(self, i):
        while 2 * i < self.maxHeapLen:
            if (2 * i + 1 < self.maxHeapLen and
                self.nums[2 * i + 1] > self.nums[2 * i] and
                self.nums[i] < self.nums[2 * i + 1]):
                self.nums[i], self.nums[2 * i + 1] = self.nums[2 * i + 1], self.nums[i]
                i = 2 * i + 1
            elif self.nums[i] < self.nums[2 * i]:
                self.nums[i], self.nums[2 * i] = self.nums[2 * i], self.nums[i]
                i = 2 * i
            else:
                break