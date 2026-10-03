class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        c = 0

        for n in nums:
            if not count:
                c = n
                count += 1
                continue
            count += (1 if c == n else -1)
        return c