class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        res = []
        for num, cnt in freq.items():
            if cnt > len(nums) // 3:
                res.append(num)
        return res