class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToindex = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in valueToindex:
                return [valueToindex[diff], i]
            valueToindex[n] = i