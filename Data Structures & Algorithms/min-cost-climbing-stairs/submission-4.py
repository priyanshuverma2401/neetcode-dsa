class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0 for _ in range(len(cost)+1)]
        min_cost[len(cost)] = float("infinity")
        min_cost[len(cost)-1] = cost[-1]

        if len(cost) >= 1:
            min_cost[len(cost)-2] = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            min_cost[i] = cost[i] + min(min_cost[i+1], min_cost[i+2])
        
        return min(min_cost[0], min_cost[1])
        
        