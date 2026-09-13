class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(cap):
            ship = 1
            curWeight = 0
            for w in weights:
                if curWeight + w > cap:
                    ship += 1
                    curWeight = 0
                curWeight += w
            return ship <= days

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                r = m - 1
            else:
                l = m + 1
        return l