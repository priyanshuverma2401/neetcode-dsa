class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sorted_nums = sorted(nums)
        # left, right = 0, len(sorted_nums)-1
        # while left < right:
        #     sum_ = sorted_nums[left] + sorted_nums[right]
        #     if sum_ == target: 
        #         return [left, right]
        #     elif sum_ < target:
        #         left += 1
        #     else:
        #         right-=1

        # brute force approach
        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        freq = dict()
        for index, ele in enumerate(nums):
            req = target - ele
            if req in freq.keys():
                return [freq[req], index]
            freq[ele] = index
        



        

        
        