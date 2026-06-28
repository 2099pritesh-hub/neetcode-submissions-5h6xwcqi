class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prevRow = [0] * (n + 1)

        for r in range(m):
            curRow = [0] * (n + 1)
            for c in range(n):
                if text1[r] == text2[c]:
                    curRow[c + 1] = 1 + prevRow[c]
                else:
                    curRow[c + 1] = max(prevRow[c + 1], curRow[c])
            prevRow = curRow
        return prevRow[n]