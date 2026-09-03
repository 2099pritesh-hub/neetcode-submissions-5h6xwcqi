class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        res = n + 1
        for i in range(n):
            l, r = i + 1, n
            while l < r:
                m = (l + r) // 2
                curSum = prefixSum[m] - prefixSum[i]
                if curSum < target:
                    l = m + 1
                else:
                    r = m

            if prefixSum[l] - prefixSum[i] >= target:
                res = min(res, l - i)

        return res if res != n + 1 else 0