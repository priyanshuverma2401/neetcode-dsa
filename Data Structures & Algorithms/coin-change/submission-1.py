class Solution:
    def countChange(self, index, amount, coins, dp):
        if amount == 0: return 0
        if index == 0:
            if amount % coins[index] == 0: return int(amount / coins[index])
            return float("infinity")
        
        if dp[index][amount] is not None: return dp[index][amount]

        not_take = 0 + self.countChange(index-1, amount, coins, dp)
        take = float("infinity")
        if coins[index] <= amount:
            take = 1 + self.countChange(index, amount - coins[index], coins, dp)
        
        dp[index][amount] = min(take, not_take)
        return dp[index][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount  == 0: return 0
        dp = [[None for _ in range(amount + 1)] for _ in range(len(coins))]
        res = self.countChange(len(coins)-1, amount, coins, dp)
        return res if res != float("infinity") else -1
        