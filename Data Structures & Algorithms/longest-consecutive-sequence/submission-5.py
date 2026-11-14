class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)# O(N)
        maxLen = 0

        for i in range(len(nums)):#O(N)
            if nums[i]-1 in NumSet:
                continue
            else:
                length = 0
                while nums[i] + length in NumSet:# O(N)
                    length+=1
                maxLen = max(maxLen, length)
        return maxLen

# Time Complexity: O(N^2)
# Space Complexity: (N)
                

        