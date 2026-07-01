class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        result = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while k:
            dist, x, y = heapq.heappop(maxHeap)
            result.append([x, y])
            k -= 1

        return result