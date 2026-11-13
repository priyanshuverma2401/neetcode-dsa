class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.PrefixSumMat = [[0 for _ in range(self.COLS+1)] for _ in range(self.ROWS+1)]

        for r in range(self.ROWS):
            prefix = 0
            for c in range(self.COLS):
                prefix += matrix[r][c]
                above = self.PrefixSumMat[r][c+1]
                self.PrefixSumMat[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        above = self.PrefixSumMat[row1-1][col2]
        left = self.PrefixSumMat[row2][col1-1]
        return (self.PrefixSumMat[row2][col2] - above - left) + self.PrefixSumMat[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)