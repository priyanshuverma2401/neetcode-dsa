class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(2*(len(nums)))]
        n = len(nums)

        for i in range(len(nums)):
            ans[i] = ans[i + n] = nums[i]
        
        return ans
        