class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        # freq = [0 for _ in range(26)]
        charSet = set()
        left = 0
        max_sub = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left +=1
            charSet.add(s[right])
            max_sub = max(max_sub, (right - left)+1)
        return max_sub



        