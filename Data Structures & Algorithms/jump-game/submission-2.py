class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums)-1
        track = [False for _ in range(len(nums))]
        track[len(nums)-1] = True

        for i in range(len(nums)-2, -1, -1):
            if goalIndex - i <= nums[i]:
                track[i] = True
                goalIndex = i
        return track[0]


        