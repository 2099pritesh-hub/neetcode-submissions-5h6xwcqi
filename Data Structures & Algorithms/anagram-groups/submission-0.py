class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            c = ''.join(sorted(s))
            if c in res:
                res[c].append(s)
            else:    
                res[c] = [s]
        return [i for i in res.values()]