class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if l < r and people[r] + people[l] <= limit:
                l += 1
            r -= 1
            res += 1
        return res