class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -(stones[i])

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = abs(heapq.heappop(stones))
            stone_2 = abs(heapq.heappop(stones))

            if stone_1 > stone_2:
                heapq.heappush(stones, -(stone_1 - stone_2))
        
        return abs(stones[0]) if stones else 0