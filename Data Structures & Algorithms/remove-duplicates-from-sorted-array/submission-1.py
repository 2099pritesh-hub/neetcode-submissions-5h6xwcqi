class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            nums[k] = n
            k += 1
        return k