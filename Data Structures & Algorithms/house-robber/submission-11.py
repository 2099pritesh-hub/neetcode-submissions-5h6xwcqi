class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = skip = 0

        for i in range(len(nums) - 1, -1, -1):
            skip, rob = max(nums[i] + rob, skip), skip
        return skip