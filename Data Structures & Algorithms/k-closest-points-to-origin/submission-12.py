class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = [(x*x + y*y, x, y) for x, y in points]
        
        heapq.heapify(minHeap)

        while k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res