class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            total = 0
            for c in range(n):
                total += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = total + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMatrix[row2][col2]
        bottomLeft = self.sumMatrix[row2][col1 - 1]
        topRight = self.sumMatrix[row1 - 1][col2]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        return bottomRight - bottomLeft - topRight + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)