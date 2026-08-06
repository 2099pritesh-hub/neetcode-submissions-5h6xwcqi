class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            count = tuple(count)
            if count in groups:
                groups[count].append(s)
            else:
                groups[count] = [s]
        return [val for val in groups.values()]
