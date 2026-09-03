class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        res = n + 1
        for i in range(n):
            l, r = i, n - 1
            while l < r:
                m = (l + r) // 2
                if i == 0:
                    curSum = prefixSum[m]
                else:
                    curSum = prefixSum[m] - prefixSum[i - 1]
                if curSum < target:
                    l = m + 1
                else:
                    r = m

            if i == 0:
                    curSum = prefixSum[l]
            else:
                curSum = prefixSum[l] - prefixSum[i - 1]

            if  curSum >= target:
                res = min(res, l - i + 1)
        return res if res != n + 1 else 0