class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                m = (l + r) // 2
                curSum = prefixSum[m + 1] - prefixSum[i]
                if curSum < target:
                    l = m + 1
                else:
                    r = m

            if l != n:
                res = min(res, l - i + 1)

        return res if res != n + 1 else 0