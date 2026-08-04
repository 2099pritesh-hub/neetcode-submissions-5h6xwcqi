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
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if right < heapLen and arr[largest] < arr[right]:
                largest = right
            if left < heapLen and arr[largest] < arr[left]:
                largest = left
            if largest == i:
                break
            
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest