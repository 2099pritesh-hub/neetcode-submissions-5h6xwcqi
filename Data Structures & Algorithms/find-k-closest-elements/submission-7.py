class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr): return arr
        l = 0
        for r in range(k, len(arr)):
            if arr[r] == arr[l]:
                l += 1
            elif abs(arr[l] - x) < abs(arr[r] - x):
                return arr[l:r]
            elif abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                return arr[l:r]
        return arr[l:r + 1]