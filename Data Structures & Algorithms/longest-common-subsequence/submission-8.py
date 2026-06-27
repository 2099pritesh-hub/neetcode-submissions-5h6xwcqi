class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        prevRow = [0] * (COLS + 1)

        for r in range(ROWS - 1, -1, -1):
            curRow = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                if text1[r] == text2[c]:
                    curRow[c] = 1 + prevRow[c + 1]
                else:
                    curRow[c] = max(curRow[c + 1], prevRow[c])
            prevRow = curRow
        return curRow[0]