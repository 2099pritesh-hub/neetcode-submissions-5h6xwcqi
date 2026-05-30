class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        for key, value in hashMap.items():
            if value > len(nums) / 2:
                return key