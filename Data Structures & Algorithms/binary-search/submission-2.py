class Solution:
    def binarySearch(self, nums, left, right, target):
        if left > right or (left == right and nums[left] != target) : 
            return -1

        mid = (left + right) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)
        else:
            return self.binarySearch(nums, left, mid - 1, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
        