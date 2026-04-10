class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def clSt(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = clSt(n - 1) + clSt(n - 2)
            return memo[n]
        
        return clSt(n)