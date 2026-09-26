class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # preMin = [0 for _ in range(len(prices))]
        # preMin[0] = prices[0]
        # for i in range(1, len(prices)):
        #     preMin[i] = min(prices[i], preMin[i-1])
        
        # max_profit = 0
        # for i in range(len(preMin)):
        #     max_profit = max(max_profit, prices[i] - preMin[i])
        # return max_profit

        preMin = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - preMin)
            preMin = min(preMin, prices[i])
        return max_profit

        