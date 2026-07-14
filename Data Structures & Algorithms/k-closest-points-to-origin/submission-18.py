class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k -= 1

        def quickSelect(l, r):
            p = points[r]
            distPivot = (p[0] ** 2) + (p[1] ** 2)

            i = l
            for j in range(l, r):
                dist = (points[j][0] ** 2) + (points[j][1] ** 2)
                if dist < distPivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[r] = points[r], points[i]

            if i < k:
                return quickSelect(i + 1, r)
            elif i > k:
                return quickSelect(l, i - 1)
            else:
                return points[:k + 1]
        
        return quickSelect(0, len(points) - 1)