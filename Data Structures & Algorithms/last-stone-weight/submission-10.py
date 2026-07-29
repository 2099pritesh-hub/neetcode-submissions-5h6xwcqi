class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 < s2:
                heapq.heappush(stones, s1 - s2)

        return abs(stones[0]) if stones else 0