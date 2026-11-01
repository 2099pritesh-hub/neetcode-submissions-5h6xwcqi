class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        def split(l, r):
            if l == r:
                return
            
            m = (l + r) // 2
            split(l, m)
            split(m + 1, r)
            merge(l, r, m)
        
        def merge(l, r, m):
            L = nums[l:m + 1]
            R = nums[m + 1: r + 1]
            i = l
            j = k = 0
            while j < len(L) and k < len(R):
                if L[j] <= R[k]:
                    nums[i] = L[j]
                    j += 1
                else:
                    nums[i] = R[k]
                    k += 1
                i += 1
            while j < len(L):
                nums[i] = L[j]
                i += 1
                j += 1
            while k < len(R):
                nums[i] = R[k]
                i += 1
                k += 1
        
        split(0, len(nums) - 1)
        return nums
            