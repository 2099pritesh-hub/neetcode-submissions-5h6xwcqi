import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(l, r):
            if l >= r:
                return
            
            pivotIndex = random.randint(l, r)
            nums[r], nums[pivotIndex] = nums[pivotIndex], nums[r]
            pivot = nums[r]
            j = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            
            nums[j], nums[r] = nums[r], nums[j]

            quickSort(l, j-1)
            quickSort(j+1, r)
        
        quickSort(0, len(nums) - 1)
        return nums