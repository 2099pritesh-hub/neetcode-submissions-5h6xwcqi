class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        l, r = 1, maxK
        k = maxK

        while l <= r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            
            if time > h:
                l = m + 1
            else:
                r = m - 1
                k = m
        return k