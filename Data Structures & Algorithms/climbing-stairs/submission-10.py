class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(cur, cache):
            if cur <= 0:
                return cur == 0
            if cur in cache:
                return cache[cur]
            
            cache[cur] = dfs(cur - 1, cache) + dfs(cur - 2, cache)
            return cache[cur]
        
        return dfs(n, {})