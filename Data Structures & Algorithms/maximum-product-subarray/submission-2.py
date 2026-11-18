class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix, prefix = 1, 1
        maxProduct = -float("infinity")
        n = len(nums)

        for i in range(len(nums)):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]

            maxProduct = max(maxProduct, prefix, suffix)
        
        return maxProduct

        
        