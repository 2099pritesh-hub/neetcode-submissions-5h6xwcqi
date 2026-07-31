class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(0, len(nums) - 1, nums)
        return nums
    
    def divide(self, s, e, arr):
        if s >= e:
            return
        
        m = (s + e) // 2
        self.divide(s, m, arr)
        self.divide(m + 1, e, arr)
        self.merge(s, m , e, arr)
    
    def merge(self, s, m, e, arr):
        left = arr[s: m + 1]
        right = arr[m + 1: e + 1]

        i = 0
        j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1