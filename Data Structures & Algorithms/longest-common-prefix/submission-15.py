class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, c in enumerate(strs[0]):
            for s in strs:
                if len(s) == i or s[i] != c:
                    return strs[0][:i]
        return strs[0]