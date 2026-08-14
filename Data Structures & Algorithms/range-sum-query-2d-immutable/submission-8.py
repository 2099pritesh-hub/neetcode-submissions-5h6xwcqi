class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * n for _ in range(m)]
        for r in range(m):
            total = 0
            for c in range(n):
                total += matrix[r][c]
                self.sumMatrix[r][c] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.sumMatrix[r][col2]
            total -= self.sumMatrix[r][col1 - 1] if (col1 - 1) >= 0 else 0
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)