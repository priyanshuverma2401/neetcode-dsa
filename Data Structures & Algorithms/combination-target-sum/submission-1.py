class Solution:
    def dfs(self, index, nums, subset, target):
        if index == len(nums):
            if target == 0: self.res.append(subset[:])
            return
        
        if nums[index] <= target:
            subset.append(nums[index])
            self.dfs(index, nums, subset, target - nums[index])
            subset.pop()
        
        self.dfs(index+1, nums, subset, target)
        return

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(0, nums, [], target)
        return self.res
        