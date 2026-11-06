class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0 : 1}
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in hashMap:
                res += hashMap[diff]
            hashMap[curSum] = 1 + hashMap.get(curSum, 0)
        return res