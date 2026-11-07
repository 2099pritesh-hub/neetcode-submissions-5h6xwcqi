class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)
            if 0 < val <= n:
                if nums[val - 1] == 0:
                    nums[val - 1] = -num
                elif nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        return n + 1