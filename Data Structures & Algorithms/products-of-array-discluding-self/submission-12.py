class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProd = [1] * n
        suffProd = [1] * n
        res = [0] * n

        for i in range(1, n):
            preProd[i] = preProd[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffProd[i] = suffProd[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = preProd[i] * suffProd[i]
        return res