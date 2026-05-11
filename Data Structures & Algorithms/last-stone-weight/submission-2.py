class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -abs(stones[i])
        
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = abs(heapq.heappop(stones))
            s2 = abs(heapq.heappop(stones))

            if s1 > s2:
                heapq.heappush(stones, -abs(s1 - s2))

        return abs(stones[0]) if stones else 0