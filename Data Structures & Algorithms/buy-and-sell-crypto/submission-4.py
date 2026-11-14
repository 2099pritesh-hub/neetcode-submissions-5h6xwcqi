class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                maxProfit = max(maxProfit, profit)
        return maxProfit