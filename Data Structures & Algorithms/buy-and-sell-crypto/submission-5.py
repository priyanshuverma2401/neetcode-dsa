class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix_min_arr = [0]*len(prices) #O(N)
        suffix_max_arr = [0]*len(prices) #O(N)
        max_profit = 0

        # building prefix min array
        prefix_min_arr[0] = prices[0]
        for i in range(1, len(prefix_min_arr)): #O(N)
            prefix_min_arr[i] = min(prices[i-1], prefix_min_arr[i-1])
        
        # creating suffix max array
        suffix_max_arr[len(prices)-1] = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1): #O(N)
            suffix_max_arr[i] = max(prices[i], suffix_max_arr[i+1])

        for i in range(len(prices)): #O(N)
            max_profit = max(max_profit, (suffix_max_arr[i] - prefix_min_arr[i]))
        
        return max_profit

# Time complexity: O(N)
# Space complexity: O(n)
        
        
        