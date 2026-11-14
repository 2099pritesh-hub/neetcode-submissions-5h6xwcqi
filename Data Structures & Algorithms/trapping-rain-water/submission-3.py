class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height) - 1):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        res = 0
        for i, h in enumerate(height):
            water = min(maxLeft[i], maxRight[i]) - h
            if water > 0:
                res += water
        return res