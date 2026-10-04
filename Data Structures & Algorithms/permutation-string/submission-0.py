class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        s2_freq = [0]*26
        k = len(s1)

        for c in s1: #o(N)
            s1_freq[ord(c) - ord('a')] += 1

        left = 0
        for right in range(len(s2)): #O(N)
            while ((right - left) + 1) > k:
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left+=1
            
            s2_freq[ord(s2[right]) - ord('a')] += 1
            if s1_freq == s2_freq: return True
        return False

# Time complexity: O(26.N) ~ O(N)
# Space complexity: O(26) ~ O(1)

        