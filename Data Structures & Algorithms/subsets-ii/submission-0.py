class Solution:
    def findSubsets(self, nums, index, subset):
        if index == len(nums):
            self.res.append(subset[:])
            return

        # decision to take the current element
        subset.append(nums[index])
        self.findSubsets(nums, index+1, subset)
        subset.pop()

        # decision to not take the current element
        current = nums[index]
        while index < len(nums) and current == nums[index]:
            index+=1

        self.findSubsets(nums, index, subset)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.findSubsets(nums, 0, [])
        return self.res
        