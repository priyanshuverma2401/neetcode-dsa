import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)

        left, right, res = 1, maxPiles, maxPiles
        

        while left <= right:
            k = (left + right) // 2
            # print(k)
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            # print(f"k = {k} hours = {hours}")
            
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res
        