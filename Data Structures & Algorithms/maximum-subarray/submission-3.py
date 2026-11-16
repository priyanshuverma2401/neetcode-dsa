class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0 for _ in range(len(nums))]
        maxSum = nums[0]
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            if prefix_sum[i-1] < 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]
            
            maxSum = max(maxSum, prefix_sum[i])
        
        return maxSum
            
        