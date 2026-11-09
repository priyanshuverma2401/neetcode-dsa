class Solution:
    def reachLast(self, nums, index, dp):
        if index == len(nums)-1: return True

        if dp[index] != None: return dp[index]

        for i in range(1, nums[index]+1):
            if self.reachLast(nums, index + i, dp): 
                dp[index] = True
                return dp[index]
        dp[index] = False
        return dp[index]
        

    def canJump(self, nums: List[int]) -> bool:
        dp = [None for _ in range(len(nums))]
        return self.reachLast(nums, 0, dp)