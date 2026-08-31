class Solution:
    def isPalindrome(self, s: str) -> bool:

        def alphaNumeric(i):
            return (ord("a") <= ord(s[i]) <= ord("z") or
                    ord("A") <= ord(s[i]) <= ord("Z") or
                    ord("0") <= ord(s[i]) <= ord("9"))

        l, r = 0, len(s) - 1
        while l < r:
            while not alphaNumeric(l) and l < r:
                l += 1
            while not alphaNumeric(r) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True