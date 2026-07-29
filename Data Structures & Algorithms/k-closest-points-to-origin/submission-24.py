class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def quickSelect(l, r):
            x, y = points[r]
            pivotDist = x*x + y*y

            i = l
            for j in range(l, r):
                X, Y = points[j]
                dist = X*X + Y*Y
                if dist <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[r] = points[r], points[i]
            
            if i < k-1:
                return quickSelect(i + 1, r)
            elif i > k-1:
                return quickSelect(l, i - 1)
            else:
                return points[:i+1]
        
        return quickSelect(0, len(points) - 1)