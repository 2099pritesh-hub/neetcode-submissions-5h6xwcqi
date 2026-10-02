class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToindex = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in valueToindex:
                return [valueToindex[diff], i]
            valueToindex[val] = i