class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplet = []
        # for i in range(len(nums)):
        #     first_ele = nums[i]
        #     required = 0 - first_ele
        #     numSet = set()
        #     for j in range(i + 1, len(nums)):
        #         tar = required - nums[j]
        #         if tar in numSet:
        #             triplet.append([first_ele, nums[j], tar])
        #         numSet.add(nums[j])
        # return triplet


        # eliminating duplicates from result triplet

        sorted_nums = sorted(nums)
        triplet = []
        for i in range(len(nums)):
            if i > 0:
                if sorted_nums[i] == sorted_nums[i-1]:
                    continue
            target = 0 - sorted_nums[i]
            left = i + 1
            right = len(sorted_nums)-1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] == target:
                    triplet.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]: left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right+1]: right-=1
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left+=1
                else:
                    right -= 1
        return triplet

            
            

        