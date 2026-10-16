class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in valueToIndex:
                return [valueToIndex[diff], i]
            valueToIndex[num] = i