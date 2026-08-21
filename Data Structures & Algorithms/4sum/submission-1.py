class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        fourSum = nums[i] + nums[j] + nums[k] + nums[l]
                        if fourSum == target:
                            res.add((nums[i], nums[j], nums[k], nums[l]))
        return list(res)