class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [0] * (N + 1)

        for r in range(M - 1, -1, -1):
            diag = 0
            for c in range(N - 1, -1, -1):
                temp = dp[c]
                if text1[r] == text2[c]:
                    dp[c] = 1 + diag
                else:
                    dp[c] = max(dp[c], dp[c + 1])
                diag = temp
        return dp[0]