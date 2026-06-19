class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(2):
            nums.append(0)
        
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i + 2] + nums[i], nums[i + 1])
        return nums[0]