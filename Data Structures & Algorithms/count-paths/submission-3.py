class Solution:
    def memoization(self, row, col, ROWS, COLS, dp):
        if row == ROWS-1 and col == COLS-1:
            return 1
        elif row >= ROWS or col >= COLS: return 0

        if dp[row][col] is not None: return dp[row][col]

        # going DOWN
        down = self.memoization(row+1, col, ROWS, COLS, dp)
        # going RIGHT
        right = self.memoization(row, col+1, ROWS, COLS, dp)

        dp[row][col] = down + right
        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        dp = [[None for _ in range(n)] for _ in range(m)]
        self.memoization(0, 0, m, n, dp)
        return dp[0][0]
        