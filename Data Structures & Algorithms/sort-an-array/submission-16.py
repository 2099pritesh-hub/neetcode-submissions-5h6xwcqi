class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            m = (l + r) // 2
            candidates = [(nums[l], l), (nums[m], m), (nums[r], r)]
            candidates.sort()
            pivotIndex = candidates[1][1]
            nums[r], nums[pivotIndex] = nums[pivotIndex], nums[r]

            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[r] = nums[r], nums[i]

            quickSort(l, i - 1)
            quickSort(i + 1, r)
        
        quickSort(0, len(nums) - 1)
        return nums