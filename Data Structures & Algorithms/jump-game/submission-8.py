class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums)-1
        track = [False for _ in range(len(nums))]
        track[goalIndex] = True

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= (goalIndex - i):
                track[i] = True
                goalIndex = i
        return track[0]
        