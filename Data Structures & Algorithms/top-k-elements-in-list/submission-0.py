import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        queue = []
        freq = dict()
        for ele in nums:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        for key, value in freq.items():
            heapq.heappush(queue, (-value, key))
        
        res = []
        while k and queue:
            priority, ele = heapq.heappop(queue)
            res.append(ele)
            k-=1
        return res




        