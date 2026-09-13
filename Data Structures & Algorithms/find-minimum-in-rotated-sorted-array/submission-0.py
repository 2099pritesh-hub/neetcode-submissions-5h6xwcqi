class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = max(nums)
        for n in nums:
            m = min(m, n)
        return m