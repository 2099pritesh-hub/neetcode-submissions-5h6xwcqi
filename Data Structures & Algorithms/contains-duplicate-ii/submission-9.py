class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        l = 0
        for n in nums:
            if len(hashSet) >= (k + 1):
                hashSet.remove(nums[l])
                l += 1
            if n in hashSet:
                return True
            hashSet.add(n)
        return False