class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}

        for i in range(len(nums)):
            req = target - nums[i]
            if req in seen_map.keys():
                return [i, seen_map[req]] if i < seen_map[req] else [seen_map[req], i]
            seen_map[nums[i]] = i
        