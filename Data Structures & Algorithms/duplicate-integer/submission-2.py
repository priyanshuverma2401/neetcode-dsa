class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_ele = set()
        for ele in nums:
            if ele in seen_ele:
                return True
            seen_ele.add(ele)
        return False
        