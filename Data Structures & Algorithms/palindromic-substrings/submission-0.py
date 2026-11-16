class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # if s is of odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left -= 1
                right += 1
            
            # if s is of even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left -= 1
                right += 1
            
        return count
            
        