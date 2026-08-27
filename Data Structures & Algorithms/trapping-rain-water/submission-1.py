class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        
        res = 0
        for i in range(n):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if water > 0:
                res += water
        return res