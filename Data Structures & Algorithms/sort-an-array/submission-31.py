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
            
            i = s
            j = 0
            k = 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        divide(0, len(nums) - 1)
        return nums