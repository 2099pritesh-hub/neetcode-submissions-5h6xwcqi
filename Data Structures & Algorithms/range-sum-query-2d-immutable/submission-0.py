class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def dfs(r, c, visit):
            if r > row2 or c > col2:
                return 0
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            total = self.matrix[r][c]
            total += dfs(r + 1, c, visit)
            total += dfs(r, c + 1, visit)
            return total
        
        return dfs(row1, col1, set())

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)