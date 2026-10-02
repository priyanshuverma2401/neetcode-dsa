class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #O(N log N)
        
        for i in range(len(nums)): #O(N)
            if i > 0 and nums[i] == nums[i-1]: 
                 continue
                
            left, right = i+1, len(nums)-1
            while left < right: #O(N)
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > 0:
                    right-=1
                elif three_sum < 0: 
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return res

# Time Complexity: O(N) + O(N log N) = O(N log N)
# Space complexity: O(N)
        