class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSum = 0

        def dfs(i, cur, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if i == len(nums) or curSum > target:
                return

            cur.append(nums[i])
            curSum += nums[i]
            dfs(i, cur, curSum)
            cur.pop()
            curSum -= nums[i]
            dfs(i + 1, cur, curSum)
        
        dfs(0, [], 0)
        return res