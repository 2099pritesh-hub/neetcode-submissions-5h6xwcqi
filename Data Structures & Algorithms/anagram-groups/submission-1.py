class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            count = tuple(count)
            if count in res:
                res[count].append(s)
            else:
                res[count] = [s]
                
        ans = []
        for grp in res.values():
            ans.append(grp)
        return ans