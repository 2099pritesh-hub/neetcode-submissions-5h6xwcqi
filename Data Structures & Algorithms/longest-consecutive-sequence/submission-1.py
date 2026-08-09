class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        j = nums[0]
        length = 1
        res = 0

        for i in range(1, len(nums)):
            if nums[i] == j:
                continue

            if nums[i] == (j + 1):
                length += 1
                j = nums[i]
            else:
                res = max(length, res)
                length = 1
                j = nums[i]
        res = max(length, res)
        return res