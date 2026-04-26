class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frequency = [0] * 3

        for num in nums:
            frequency[num] += 1
        
        i = 0
        for _ in range(len(frequency)):
            for j in range(0, frequency[_]):
                nums[i] = _
                i += 1
        return nums