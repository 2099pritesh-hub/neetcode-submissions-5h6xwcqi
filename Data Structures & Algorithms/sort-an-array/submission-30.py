class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(s, e):
            if s >= e:
                return None
            m = (s + e) // 2
            divide(s, m)
            divide(m + 1, e)
            merge(s, m, e)
        
        def merge(s, m, e):
            L = nums[s: m + 1]
            R = nums[m + 1: e + 1]

            i = s
            j = 0
            k = 0

            while j < len(L) and k < len(R):
                if L[j] < R[k]:
                    nums[i] = L[j]
                    j += 1
                else:
                    nums[i] = R[k]
                    k += 1
                i += 1
            
            while j < len(L):
                nums[i] = L[j]
                j += 1
                i += 1
            while k < len(R):
                nums[i] = R[k]
                k += 1
                i += 1

        divide(0, len(nums) - 1)
        return nums