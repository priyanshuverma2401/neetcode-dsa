class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        maxLen = 0

        for i in range(len(nums)):
            if nums[i]-1 in NumSet:
                continue
            else:
                length = 0
                while nums[i] + length in NumSet:
                    length+=1
                maxLen = max(maxLen, length)
        return maxLen
                

        