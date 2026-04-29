class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            m = (l + r) // 2

            row = m // len(matrix[0])
            column = m % len(matrix[0])

            if matrix[row][column] < target:
                l = m + 1
            elif matrix[row][column] > target:
                r = m - 1
            else:
                return True
        return False 