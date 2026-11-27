class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # print(max(7, 4, 12))
        good = [None for _ in range(3)]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for index, value in enumerate(t):
                if value == target[index]:
                    good[index] = value
        
        return True if None not in good else False
        

        