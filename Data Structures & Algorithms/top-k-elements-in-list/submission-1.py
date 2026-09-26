import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # queue = []
        # freq = dict()
        # for ele in nums:
        #     if ele in freq:
        #         freq[ele] += 1
        #     else:
        #         freq[ele] = 1

        # for key, value in freq.items():
        #     heapq.heappush(queue, (-value, key))
        
        # res = []
        # while k and queue:
        #     priority, ele = heapq.heappop(queue)
        #     res.append(ele)
        #     k-=1
        # return res


        # using bucket sort algorithm
        freq_map = dict()
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for ele in nums:
            freq_map[ele] = 1 + freq_map.get(ele, 0)
        
        for ele, frequency in freq_map.items():
            freq_arr[frequency].append(ele)
        
        res = []
        for l in range(len(freq_arr)-1, 0, -1):
            for i in range(len(freq_arr[l])):
                res.append(freq_arr[l][i])
                if len(res) == k: return res
        return

        





        