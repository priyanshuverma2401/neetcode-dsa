class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right: #O(N)
            sum_ = numbers[left] + numbers[right]
            if sum_ == target: return [left + 1, right + 1]
            elif sum_ < target: left+=1
            else: right-=1

# Time complexity: O(N)
# Space Complexity: O(1)
        