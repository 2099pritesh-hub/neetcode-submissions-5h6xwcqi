class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[k - 1]:
                continue
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
        return k