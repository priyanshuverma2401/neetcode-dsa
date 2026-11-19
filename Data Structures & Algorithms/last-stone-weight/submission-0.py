class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-x for x in stones]
        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            firstStone = - (heapq.heappop(stoneHeap))
            secondStone = - (heapq.heappop(stoneHeap))

            if firstStone > secondStone:
                newStone = firstStone - secondStone
                heapq.heappush(stoneHeap, -(newStone))
            elif secondStone > firstStone:
                newStone = secondStone - firstStone
                heapq.heappush(stoneHeap, -(newStone))
        return - stoneHeap[0] if len(stoneHeap) > 0 else 0
        