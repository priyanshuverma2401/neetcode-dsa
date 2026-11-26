class Solution:
    def countSetBit(self, num):
        count = 0
        while num:
            count += (num & 1)
            num >>= 1
        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countSetBit(i))
        return res
        