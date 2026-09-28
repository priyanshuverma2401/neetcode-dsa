class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*len(nums) #O(N)
        right_product = [1]*len(nums) #O(N)
        response = [1]*len(nums) #O(N)

        # calculating left product:
        for i in range(1, len(nums)): #O(N)
            left_product[i] = nums[i-1] * left_product[i-1]
        
        # calculating right product
        for i in range(len(nums)-2, -1, -1): #O(N)
            right_product[i] = nums[i+1] * right_product[i+1]
        
        #calculating result
        for i in range(len(nums)): #O(N)
            response[i] = left_product[i] * right_product[i]
        
        return response

# Time Complexity: O(N) + O(N) + O(N) = O(N)
# Space Complexity: O(N) + O(N) + O(N) = O(N)
        