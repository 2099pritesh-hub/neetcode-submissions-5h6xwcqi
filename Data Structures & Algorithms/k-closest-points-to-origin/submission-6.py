class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(len(points)):
            dist = -(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(maxHeap, [dist, points[i][0], points[i][1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res