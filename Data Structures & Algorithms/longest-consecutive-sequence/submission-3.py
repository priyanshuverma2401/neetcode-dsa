class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) #Space: O(N)
        max_length = 0

        for i in range(len(nums)): #Time: O(N)
            # checking if this is the start of sequence
            if (nums[i] - 1) not in numset:
                length = 0
                while (nums[i] + length) in numset: #Time: O(N)
                    length+=1
                max_length = max(max_length, length)
        return max_length

# Time Complexity: O(N^2)
# Space Complexity: O(N)
                
        
        