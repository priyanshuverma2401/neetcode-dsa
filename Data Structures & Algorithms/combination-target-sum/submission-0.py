class Solution:

    def findCombination(self, nums, index, target, ans, currentArr):
        if target == 0: 
            ans.append(currentArr[:])
            return
        if index < 0: return
        
        self.findCombination(nums, index - 1, target, ans, currentArr)
        if nums[index] <= target:
            currentArr.append(nums[index])
            self.findCombination(nums, index, target - nums[index], ans, currentArr)
            currentArr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findCombination(nums, len(nums)-1, target, ans, [])
        return ans
        