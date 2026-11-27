class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            reqD = 1
            cur = 0
            for w in weights:
                if cur + w <= m:
                    cur += w
                else:
                    reqD += 1
                    cur = w
            
            if reqD <= days:
                r = m - 1
            else:
                l = m + 1
        return l