class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= goalIndex - i:
                goalIndex = i
        
        # return True if goalIndex == 0 else False
        return goalIndex == 0
        