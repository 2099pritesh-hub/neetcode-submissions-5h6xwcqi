class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            freq = tuple(freq)
            if freq in group:
                group[freq].append(s)
            else:
                group[freq] = [s]
        return [v for v in group.values()]