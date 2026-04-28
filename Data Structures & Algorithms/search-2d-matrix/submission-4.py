class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                return self.findTarget(matrix[m], target)
        return False

    def findTarget(self, arr, key):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if key > arr[mid]:
                left = mid + 1
            elif key < arr[mid]:
                right = mid - 1
            else:
                return True
        return False