class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsStack = nums[:]
        heapq.heapify(numsStack)

        while len(numsStack) > k:
            heapq.heappop(numsStack)
        return numsStack[0]
        