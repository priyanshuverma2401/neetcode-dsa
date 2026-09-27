class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in freq_map:
                return [freq_map[req], i]
            freq_map[nums[i]] = i



        