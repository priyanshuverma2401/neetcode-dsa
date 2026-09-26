class Solution:
    def robMaximum(self, nums, index, dp):
        if index == 0: return nums[0]
        if index < 0: return 0

        if dp[index] != -1: return dp[index]
        dp[index] = max(self.robMaximum(nums, index-1, dp), nums[index] + self.robMaximum(nums, index - 2, dp))
        return dp[index]

        

    def rob(self, nums: List[int]) -> int:

        dp = [-1 for _ in range(len(nums))]
        return self.robMaximum(nums, len(nums)-1, dp)
        