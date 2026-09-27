class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int) #O(N)
        heap_queue = [] #O(N)
        for num in nums: #O(N) --> N is the length of nums
            freq_map[num] += 1
        

        for key, value in freq_map.items(): #O(M)
            heapq.heappush(heap_queue, (-value, key)) #(log M)
        
        res = [] #O(K)

        while k and heap_queue: #O(k)
            priority, key = heapq.heappop(heap_queue)
            res.append(key)
            k-=1
        return res

# Time Complexity: O(N) + O(M log M) + O(K log M) = O(M log m)
# N (Total number of element in nums): 6
# M (Total unique elemement in nums): 4

# Space Complexity: O(M) + O(M) + O(K) = O(N)


        