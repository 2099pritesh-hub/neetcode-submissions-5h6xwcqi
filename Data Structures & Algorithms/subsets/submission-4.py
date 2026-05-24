class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def findSubsets(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            findSubsets(i + 1, cur)
            cur.pop()
            findSubsets(i + 1, cur)
        
        findSubsets(0, [])
        return res