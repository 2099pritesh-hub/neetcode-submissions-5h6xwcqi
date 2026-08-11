class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        res = []
        for num, freq in count.items():
            if freq > len(nums) / 3:
                res.append(num)
        return res