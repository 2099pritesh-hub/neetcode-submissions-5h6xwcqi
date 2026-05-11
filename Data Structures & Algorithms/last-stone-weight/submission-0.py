class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()

            if s1 > s2:
                stones.append(s1 - s2)

        if stones:
            return stones[0]
        else:
            return 0