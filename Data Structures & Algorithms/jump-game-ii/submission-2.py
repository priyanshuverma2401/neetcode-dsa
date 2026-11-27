class Solution:
    def reachlast(self, index, nums, dp):
        if index == len(nums)-1:
            return 0
        
        if index >= len(nums):
            return float("infinity")
        
        if dp[index] != -1: return dp[index]
        
        minJump = float("inf")

        for i in range(1, nums[index]+1):
            jump = 1 + self.reachlast(index + i, nums, dp)
            minJump = min(minJump, jump)
        
        dp[index] = minJump
        return dp[index]


    def jump(self, nums: List[int]) -> int:

        dp = [-1 for _ in range(len(nums))]
        return self.reachlast(0, nums, dp)
        