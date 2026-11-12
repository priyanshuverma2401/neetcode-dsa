class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_freq = defaultdict(int)

        for ele in nums:
            element_freq[ele] += 1

        majority_ele, freq = nums[0], element_freq[nums[0]]
        
        for key, value in element_freq.items():
            if value > freq:
                majority_ele = key
                freq = value
        
        return majority_ele

        