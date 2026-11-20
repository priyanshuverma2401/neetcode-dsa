class Solution:
    def dfs(self, index, nums, subset):
        if index == len(nums):
            self.res.append(subset[:])
            return
        
        # decision taking the current index element
        subset.append(nums[index])
        self.dfs(index+1, nums, subset)
        subset.pop()
        
        # decision not taking the current Index
        self.dfs(index+1, nums, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(0, nums, [])
        return self.res

        