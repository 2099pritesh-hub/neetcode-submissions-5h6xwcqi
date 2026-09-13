class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            
            ship = 1
            curWeight = 0
            for w in weights:
                if curWeight + w > m:
                    ship += 1
                    curWeight = 0
                curWeight += w
            
            if ship <= days:
                r = m - 1
            else:
                l = m + 1
        return l