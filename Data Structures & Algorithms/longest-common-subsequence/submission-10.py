class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prevRow = [0] * (n + 1)

        for r in range(m-1, -1, -1):
            curRow = [0] * (n + 1)
            for c in range(n-1, -1, -1):
                if text1[r] == text2[c]:
                    curRow[c] = 1 + prevRow[c + 1]
                else:
                    curRow[c] = max(prevRow[c], curRow[c + 1])
            prevRow = curRow
        return prevRow[0]