class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        for num in nums:
            if 0 < abs(num) <= len(nums):
                if num < 0:
                    if not nums[abs(num) - 1] < 0:
                        if nums[abs(num) - 1] == 0:
                            nums[abs(num) - 1] = -num
                        else:
                            nums[abs(num) - 1] = -nums[abs(num) - 1]
                elif num > 0:
                    if not nums[num - 1] < 0:
                        if nums[num - 1] == 0:
                            nums[num - 1] = -num
                        else:
                            nums[num - 1] = -nums[num - 1]
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return i + 1