class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = [0] * 26
        for c in s1:
            freqs1[ord(c) - ord("a")] += 1
        
        freqs2 = [0] * 26
        l = 0
        for r in range(len(s2)):
            freqs2[ord(s2[r]) - ord("a")] += 1
            if r - l >= len(s1):
                freqs2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if freqs1 == freqs2:
                return True
        return False