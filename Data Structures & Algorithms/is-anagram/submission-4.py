class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s = {}
        hashMap_t = {}

        for char in s:
            if char in hashMap_s:
                hashMap_s[char] += 1
            else:
                hashMap_s[char] = 1
        
        for char in t:
            if char in hashMap_t:
                hashMap_t[char] += 1
            else:
                hashMap_t[char] = 1
        
        return hashMap_s == hashMap_t