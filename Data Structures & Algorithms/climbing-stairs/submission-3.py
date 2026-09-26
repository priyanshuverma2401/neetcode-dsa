class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        two_step, one_step = 1, 2
        total_ways = 0
        for i in range(3, n+1):
            total_ways = one_step + two_step
            two_step = one_step
            one_step = total_ways
        return total_ways

