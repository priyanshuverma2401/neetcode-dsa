class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res = [], []

        for x, y in points:
            distance = (x**2) + (y**2)
            heapq.heappush(heap, [distance, x, y])
        
        while k:
            dis, xc, yc = heapq.heappop(heap)
            res.append([xc, yc])
            k-=1
        
        return res
        


        