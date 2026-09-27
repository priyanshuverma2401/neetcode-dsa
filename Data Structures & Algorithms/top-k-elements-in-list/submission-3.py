class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        heap_queue = []
        for num in nums:
            freq_map[num] += 1
        
        # print(freq_map)

        for key, value in freq_map.items():
            heapq.heappush(heap_queue, (-value, key))
        
        res = []

        # print(heapq.heappop(heap_queue))
        # print(heapq.heappop(heap_queue))
        # print(heapq.heappop(heap_queue))

        while k and heap_queue:
            priority, key = heapq.heappop(heap_queue)
            res.append(key)
            k-=1
        return res

        