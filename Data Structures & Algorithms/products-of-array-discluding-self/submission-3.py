class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix_product, postfix_product = 1, 1

        # calculating prefix
        for i in range(len(nums)): #O(N)
            res[i] = res[i] * prefix_product
            prefix_product = prefix_product * nums[i]

        # calculating postfix
        for i in range(len(nums)-1, -1, -1): #O(N)
            res[i] = res[i] * postfix_product
            postfix_product = postfix_product * nums[i]
        
        return res

# Time Complexity: O(N) + O(N) = O(N)
# Space complexity: O(1)

        