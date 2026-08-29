class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minP = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minP:
                minP = prices[i]
            else:
                res = max(res, prices[i] - minP)
        return res