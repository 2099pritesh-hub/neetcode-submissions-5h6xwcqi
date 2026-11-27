class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(cap):
            ship = 1
            cur = 0
            for w in weights:
                if cur + w <= m:
                    cur += w
                else:
                    ship += 1
                    cur = w
            return ship

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if canShip(m) <= days:
                r = m - 1
            else:
                l = m + 1
        return l