class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSum, sumList):
            if curSum == target:
                res.append(sumList.copy())
                return
            if i >= len(nums) or curSum > target:
                return
            
            sumList.append(nums[i])
            dfs(i, curSum + nums[i], sumList)

            sumList.pop()
            dfs(i + 1, curSum, sumList)

        dfs(0, 0, [])
        return res