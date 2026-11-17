class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, reslen = [-1, -1], len(s) + 1
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)
            
            if c in countT and countT[c] == countS[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    reslen = (r - l + 1)
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > countS[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if reslen != len(s) + 1 else ""