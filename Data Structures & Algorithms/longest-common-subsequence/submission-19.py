class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        prevRow = [0] * (N + 1)

        for r in range(M - 1, -1, -1):
            curRow = [0] * (N + 1)
            for c in range(N - 1, -1, -1):
                if text1[r] == text2[c]:
                    curRow[c] = 1 + prevRow[c + 1]
                else:
                    curRow[c] = max(prevRow[c], curRow[c + 1])
            prevRow = curRow
        return prevRow[0]