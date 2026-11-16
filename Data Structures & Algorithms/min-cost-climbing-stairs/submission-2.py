class Solution:
    def findMinCost(self, index, n, cost, dp):
        if index == n: return 0
        if index > n: return float("infinity")

        if dp[index] != -1: return dp[index]

        left_min_cost = cost[index] + self.findMinCost(index + 1, n, cost, dp)
        right_min_cost = cost[index] + self.findMinCost(index + 2, n, cost, dp)

        dp[index] = min(left_min_cost, right_min_cost)

        return dp[index]
 
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost) + 1)]
        # return min(self.findMinCost(0, len(cost), cost, dp), self.findMinCost(1, len(cost), cost, dp))
        self.findMinCost(0, len(cost), cost, dp)
        return min(dp[0], dp[1])
        
        