class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate = {}
        for num in nums:
            candidate[num] = 1 + candidate.get(num, 0)
            if len(candidate) > 2:
                c = {}
                for n, f in candidate.items():
                    if f > 1:
                        c[n] = f - 1
                candidate = c
        
        res = []
        for c in candidate:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
        return res