class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.maxHeapLen = len(nums)
        self.heapify(nums)
        while self.maxHeapLen > 0:
            self.pop(nums)
        return nums

    def heapify(self, arr):
        cur = self.maxHeapLen - 1

        while cur >= 0:
            i = cur
            self.percolateDown(i, arr)
            cur -= 1
    
    def pop(self, arr):
        self.maxHeapLen -= 1
        arr[0], arr[self.maxHeapLen] = arr[self.maxHeapLen], arr[0]
        i = 0
        self.percolateDown(i, arr)

    def percolateDown(self, i, arr):
        while 2 * i + 1 < self.maxHeapLen:
            if (2 * i + 2 < self.maxHeapLen and
                arr[2 * i + 2] > arr[2 * i + 1] and
                arr[i] < arr[2 * i + 2]):
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
                i = 2 * i + 2
            elif arr[i] < arr[2 * i + 1]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            else:
                break