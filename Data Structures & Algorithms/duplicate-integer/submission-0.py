from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for ele in nums:
            freq[ele] += 1
            if freq[ele] > 1: return True
        return False


        