class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(minHeap, (dist, x, y))

        while k:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
            
        return result