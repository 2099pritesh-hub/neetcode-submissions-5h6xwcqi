class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = max(piles)
        while l <= r:
            m = (l + r) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / m)
            if hour > h:
                l = m + 1
            elif hour <= h:
                res = min(res, m)
                r = m - 1
        return res