class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = min(strs)

        for i in range(len(n)):
            for j in range(1, len(strs)):
                if not strs[j]:
                    return res
                elif strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res         