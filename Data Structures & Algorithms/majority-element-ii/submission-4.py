class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
            if len(cnt) <= 2:
                continue
            newCnt = {}
            for n, c in cnt.items():
                if c > 1:
                    newCnt[n] = c - 1
            cnt = newCnt

        res = []
        for n in cnt.keys():
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res