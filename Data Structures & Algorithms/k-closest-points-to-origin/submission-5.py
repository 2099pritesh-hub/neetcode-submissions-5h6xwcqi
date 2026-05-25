class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            points[i] = [dist, points[i][0], points[i][1]]
        
        heapq.heapify(points)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(points)
            res.append([x, y])
            k -= 1
        return res