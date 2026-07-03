class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(s, cache):
            if s >= n:
                return s == n
            if s in cache:
                return cache[s]

            cache[s] = dfs(s + 1, cache) + dfs(s + 2, cache)
            return cache[s]

        return dfs(0, {})