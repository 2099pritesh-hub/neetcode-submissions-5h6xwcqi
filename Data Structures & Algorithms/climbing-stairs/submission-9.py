class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def distincyWays(n):
            if n in memo:
                return memo[n]
            if n <= 0:
                return n == 0

            memo[n] = distincyWays(n-1) + distincyWays(n-2)
            return memo[n]

        return distincyWays(n)