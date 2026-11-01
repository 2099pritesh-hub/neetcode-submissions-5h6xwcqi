class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        j = 0
        for i in range(len(count)):
            while count[i]:
                nums[j] = i
                count[i] -= 1
                j += 1