class Solution:
    def rob(self, nums: List[int]) -> int:
        next1 = next2 = 0
        for i in range(len(nums) - 1, -1, -1):
            next1, next2 = max(next2 + nums[i], next1), next1
        return next1