class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i1 = i2 = 0

        while i1 < len(word1) or i2 < len(word2):
            if i1 < len(word1):
                res.append(word1[i1])
                i1 += 1
            if i2 < len(word2):
                res.append(word2[i2])
                i2 += 1
        return ''.join(res)