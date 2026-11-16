class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[-1] = nums[-1]

        if len(nums) == 1: return nums[0]

        dp[-2] = max(nums[-1], nums[-2])

        for i in range(len(nums)-3, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]

        