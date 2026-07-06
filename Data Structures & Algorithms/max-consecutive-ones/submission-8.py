class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for n in nums:
            count = count + 1 if n else 0
            res = max(res, count)
        return res