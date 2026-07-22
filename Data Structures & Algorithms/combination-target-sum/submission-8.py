class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, curTarget):
            if curTarget == 0:
                res.append(cur.copy())
                return
            if curTarget < 0 or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, curTarget - nums[i])

            cur.pop()
            dfs(i + 1, cur, curTarget)
        
        dfs(0, [], target)
        return res