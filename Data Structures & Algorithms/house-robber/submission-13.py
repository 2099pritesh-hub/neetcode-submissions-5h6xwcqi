class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 2] + nums[i], dp[i + 1])
        return dp[0]