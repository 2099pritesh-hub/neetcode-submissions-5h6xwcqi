class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sumList = []

        def dfs(i, curSum):
            if i >= len(nums) or curSum > target:
                return
            if curSum == target:
                res.append(sumList.copy())
                return
            
            curSum += nums[i]
            sumList.append(nums[i])
            dfs(i, curSum)

            curSum -= nums[i]
            sumList.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res