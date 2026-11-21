class Solution:
    def dfs(self, index, nums, target, subset):
        if target == 0:
            self.res.append(subset[:])
            return
        
        if index == len(nums): return

        # decision to pick the current element
        if target >= nums[index]:
            subset.append(nums[index])
            self.dfs(index, nums, target - nums[index], subset)
            subset.pop()
        # decision to not pick
        self.dfs(index+1, nums, target, subset)
        return 

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(0, nums, target,[])
        return self.res
        