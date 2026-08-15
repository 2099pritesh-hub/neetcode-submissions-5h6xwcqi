class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                zero_count += 1
        
        res = [0] * len(nums)
        if zero_count > 1:
            return res
        
        for i, n in enumerate(nums):
            if zero_count and n != 0:
                res[i] = 0
            else:
                res[i] = product // n if n != 0 else product
        return res