class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0 for _ in range(len(nums))]
        max_sum = nums[0]
        
        prefix[0] = nums[0] 

        for i in range(1, len(nums)):
            if prefix[i-1] < 0:
                prefix[i] = nums[i]
                max_sum = max(max_sum, prefix[i])
            else:
                prefix[i] = prefix[i-1] + nums[i]
                max_sum = max(max_sum, prefix[i])
        
        return max_sum
