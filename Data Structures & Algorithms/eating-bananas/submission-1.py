class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l + r) // 2

            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/k)
            
            if totalHours > h:
                l = k + 1
            elif totalHours <= h:
                r = k - 1
                res = min(res, k)

        return res