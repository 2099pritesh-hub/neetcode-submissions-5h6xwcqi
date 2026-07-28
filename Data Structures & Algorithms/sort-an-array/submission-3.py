class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(nums, 0, len(nums) - 1)
        return nums

    def divide(self, arr, s, e):
        if s >= e:
            return
        
        m = (s + e) // 2

        self.divide(arr, s, m)
        self.divide(arr, m + 1, e)
        self.merge(arr, s, m, e)

    def merge(self, arr, s, m, e):
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1