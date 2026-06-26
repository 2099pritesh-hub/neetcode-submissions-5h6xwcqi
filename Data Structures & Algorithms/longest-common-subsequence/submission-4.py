class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(i1, i2):
            if i1 == ROWS or i2 == COLS:
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            
            if text1[i1] == text2[i2]:
                dp[i1][i2] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                dp[i1][i2] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            return dp[i1][i2]

        return dfs(0, 0)