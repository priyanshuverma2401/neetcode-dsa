class Solution:
    def backtrack(self, nums, subset, taken):
        if len(subset) == len(nums):
            self.res.append(subset[:])
            return
        
        for ele in nums:
            if taken.get(ele, False) == False:
                subset.append(ele)
                taken[ele] = True
                self.backtrack(nums, subset, taken)
                subset.pop()
                taken[ele] = False
        return


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res, subset = [], []
        taken = dict()
        self.backtrack(nums, subset, taken)
        return self.res

        