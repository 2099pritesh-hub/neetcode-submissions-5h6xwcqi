class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        l = r = 0

        while l < n or r < m:
            if l < n:
                res.append(word1[l])
                l += 1
            if r < m:
                res.append(word2[r])
                r += 1
        return ''.join(res)