import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            pivotIndex = random.randint(l, r)
            nums[l], nums[pivotIndex] = nums[pivotIndex], nums[l]

            pivot = nums[l]

            lt = l
            i = l
            rt = r

            while i <= rt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[rt], nums[i] = nums[i], nums[rt]
                    rt -= 1
                else:
                    i += 1

            quickSort(l, lt - 1)
            quickSort(rt + 1, r)
        
        quickSort(0, len(nums) - 1)
        return nums