class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(s, e):
            if s >= e:
                return
            
            m = (s + e) // 2
            
            divide(s, m)
            divide(m + 1, e)
            merge(s, m, e)
        
        def merge(s, m, e):
            left = nums[s: m + 1]
            right = nums[m + 1: e + 1]

            i = 0
            j = 0
            k = s

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        
        divide(0, len(nums) - 1)
        return nums