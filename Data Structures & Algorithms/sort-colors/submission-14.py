class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        i = 0
        for ind, c in enumerate(count):
            for _ in range(c):
                nums[i] = ind
                i += 1
        return nums                