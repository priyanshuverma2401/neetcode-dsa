class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)

        for i in range(1, len(nums)):
            left_product[i] = nums[i-1] * left_product[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            right_product[j] = nums[j + 1] * right_product[j+1]
        

        print(f"left product: {left_product}")
        print(f"right product: {right_product}")
        res = []

        for idx in range(len(nums)):
            if idx == 0:
                res.append(right_product[idx])
            elif idx == len(nums)-1:
                res.append(left_product[idx])
            else:
                res.append(left_product[idx] * right_product[idx])
        return res

        