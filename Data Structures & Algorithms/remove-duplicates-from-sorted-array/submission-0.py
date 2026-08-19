class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for i, n in enumerate(nums):
            if n in seen:
                continue
            nums[k] = n
            seen.add(n)
            k += 1
        return k      