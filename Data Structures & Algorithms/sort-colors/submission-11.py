class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1
        
        j = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[j] = i
                j += 1