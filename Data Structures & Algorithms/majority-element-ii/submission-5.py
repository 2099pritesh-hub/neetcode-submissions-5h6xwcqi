class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if len(count) <= 2:
                continue
            new_count = {}
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
        
        res = []
        for num in count.keys():
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res