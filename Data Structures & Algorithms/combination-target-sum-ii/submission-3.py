class Solution:
    def dfs(self, target, nums, index, subset):
        if target == 0:
            self.res.append(subset[:])
            return
        
        if index == len(nums): return

        # decision to take the current index element
        if target >= nums[index]:
            subset.append(nums[index])
            self.dfs(target-nums[index], nums, index+1, subset)
            subset.pop()

        # decision to not the current element
        current = nums[index]

        while index < len(nums) and current == nums[index]:
            index+=1
        
        self.dfs(target, nums, index, subset)
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.dfs(target, candidates, 0, [])
        # return [list(x) for x in self.res]
        return self.res
        