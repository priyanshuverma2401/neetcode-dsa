class Solution:
    def maxProfit(self, index, n, nums, dp):
        if index == n: return nums[n]
        if index > n: return 0

        if dp[index] : return dp[index]

        take = nums[index] + self.maxProfit(index + 2, n, nums, dp)
        not_take = 0 + self.maxProfit(index + 1, n, nums, dp)

        dp[index] = max(take, not_take)
        return dp[index]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        first, second= nums[1:], nums[:-1]
        dp1 = [None for _ in range(len(first))]
        dp2 = [None for _ in range(len(second))]
        return max(self.maxProfit(0, len(first)-1 , first, dp1),
                    self.maxProfit(0, len(second)-1, second, dp2))
        