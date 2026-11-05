class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate = {}
        for n in nums:
            candidate[n] = 1 + candidate.get(n, 0)
            if len(candidate) > 2:
                temp = {}
                for c, f in candidate.items():
                    if f > 1:
                        temp[c] = f - 1
                candidate = temp
        
        res = []
        for c in candidate.keys():
            if nums.count(c) > (len(nums) // 3):
                res.append(c)
        return res