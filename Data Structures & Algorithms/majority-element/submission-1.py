class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
            if hashMap[n] > maxCount:
                res = n
            maxCount = max(maxCount, hashMap[n])
        return res