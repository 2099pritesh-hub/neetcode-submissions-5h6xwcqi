class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.maxHeapLen = len(nums) + 1
        nums = self.heapify(nums)
        for i in range(len(nums) - 1, 0, -1):
            self.pop(nums)
        return nums[1:]

    def heapify(self, arr):
        arr = [0] + arr
        cur = (self.maxHeapLen - 1) // 2

        while cur > 0:
            i = cur
            self.percolateDown(i, arr)
            cur -= 1
        return arr
    
    def pop(self, arr):

        self.maxHeapLen -= 1
        arr[1], arr[self.maxHeapLen] = arr[self.maxHeapLen], arr[1]
        i = 1
        self.percolateDown(i, arr)

    def percolateDown(self, i, arr):
        while 2 * i < self.maxHeapLen:
            if (2 * i + 1 < self.maxHeapLen and
                arr[2 * i + 1] > arr[2 * i] and
                arr[i] < arr[2 * i + 1]):
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            elif arr[i] < arr[2 * i]:
                arr[i], arr[2 * i] = arr[2 * i], arr[i]
                i = 2 * i
            else:
                break