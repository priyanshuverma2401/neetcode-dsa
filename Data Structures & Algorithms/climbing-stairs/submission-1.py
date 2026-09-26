class Solution:
    def climbStairsMemoization(self, n, dp):
        if  n == 0: return 1
        if n < 0: return 0
        if dp[n] != -1: return dp[n]
        dp[n] = self.climbStairsMemoization(n-1, dp) + self.climbStairsMemoization(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:

        # if n == 0: return 1
        # if n < 0: return 0

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        dp = [-1 for _ in range(n+1)]
        return self.climbStairsMemoization(n, dp)
        

        