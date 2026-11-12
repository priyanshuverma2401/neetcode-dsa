class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, index, right = 0, 0, len(nums)-1

        def swap(i1, i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp

        while index <= right:
            if nums[index] == 0:
                swap(left, index)
                left+=1
                
            elif nums[index] == 2:
                swap(index, right)
                right-=1
                index-=1
            index+=1
        return nums


        