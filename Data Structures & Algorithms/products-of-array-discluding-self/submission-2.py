class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProd = [0] * n
        sufProd = [0] * n

        p = 1
        for i in range(n):
            p = p * nums[i]
            preProd[i] = p
        
        p = 1
        for i in range(n - 1, -1, -1):
            p = p * nums[i]
            sufProd[i] = p
        
        res = []
        for i in range(n):
            pre = preProd[i - 1] if i > 0 else 1
            suf = sufProd[i + 1] if i + 1 < n else 1
            res.append(pre * suf)
        return res