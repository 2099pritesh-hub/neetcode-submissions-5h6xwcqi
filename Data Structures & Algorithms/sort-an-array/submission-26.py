class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapify(nums)
        maxHeapLen = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[maxHeapLen - 1] = nums[maxHeapLen - 1], nums[0]
            maxHeapLen -= 1
            self.percolateDown(0, nums, maxHeapLen)
        return nums

    def heapify(self, arr):
        cur = (len(arr) // 2) - 1
        while cur >= 0:
            self.percolateDown(cur, arr, len(arr))
            cur -= 1

    def percolateDown(self, i, arr, heapLen):
        while 2 * i + 1 < heapLen:
            if (2 * i + 2 < heapLen and
                arr[2 * i + 2] > arr[2 * i + 1] and
                arr[i] < arr[2 * i + 2]):
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
                i = 2 * i + 2
            elif arr[i] < arr[2 * i + 1]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            else:
                break