class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        for c in s:
            countS[c] = 1 + countS.get(c, 0)
        
        for c in t:
            if c not in countS:
                return False
            countS[c] -= 1
            if countS[c] < 0:
                return False
        return True