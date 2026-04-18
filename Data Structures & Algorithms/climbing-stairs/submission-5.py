class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def distinctWays(n):
            if n <= 0:
                return n == 0
            if n in memo:
                return memo[n]
            
            memo[n] = distinctWays(n-1) + distinctWays(n-2)
            return memo[n]
        
        return distinctWays(n)