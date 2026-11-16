class Solution:

    def maxProfit(self, index, n, nums, dp):
        if index == n: return nums[n]
        if index > n: return 0

        if dp[index]: return dp[index]

        take = nums[index] + self.maxProfit(index + 2, n, nums, dp)
        not_take = 0 + self.maxProfit(index + 1, n, nums, dp)

        dp[index] = max(take, not_take)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        dp = [None for _ in range(len(nums))]

        return self.maxProfit(0, len(nums)-1, nums, dp)
        