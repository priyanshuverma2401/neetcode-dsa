class Solution:
    def findWays(self, n, index, dp):
        if index == n: return 1
        if index > n: return 0

        if dp[index] != -1: return dp[index]

        left_ways = self.findWays(n, index+1, dp)
        right_ways = self.findWays(n, index + 2, dp)

        dp[index] = left_ways + right_ways
        return dp[index]

    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        return self.findWays(n, 0, dp)
        