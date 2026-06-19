class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            a, b = max(b + nums[i], a), a
        return a