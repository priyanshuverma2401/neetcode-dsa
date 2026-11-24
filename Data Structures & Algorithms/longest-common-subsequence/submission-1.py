class Solution:
    def memoization(self, index1, index2, text1, text2, dp):
        if index1 < 0 or index2 < 0:
            return 0
        
        if dp[index1][index2] != -1:
            return dp[index1][index2]

        if text1[index1] == text2[index2]:
            return 1 + self.memoization(index1-1, index2-1, text1, text2, dp)

        dp[index1][index2] = max(self.memoization(index1-1, index2, text1, text2, dp),
                    self.memoization(index1, index2-1, text1, text2, dp)) 
        return dp[index1][index2]

  
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.memoization(len(text1)-1, len(text2)-1, text1, text2, dp)

        