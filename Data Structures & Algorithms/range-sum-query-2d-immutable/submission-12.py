class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(row):
            rowSum = 0
            for c in range(col):
                rowSum += matrix[r][c]
                self.sumMatrix[r + 1][c + 1] = rowSum + self.sumMatrix[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        total = self.sumMatrix[row2][col2]
        topRight = self.sumMatrix[row1 - 1][col2]
        bottomLeft = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        return total - topRight - bottomLeft + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)