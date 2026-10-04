class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #O(26)
        res = 0
        left = 0

        for right in range(len(s)): #O(N)
            count[s[right]] = 1 + count.get(s[right], 0)

            while ((right - left) + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, ((right - left) + 1))
        return res

# Time Complexity: O(26.N) = O(N)
# Space complexity: O(1)

        
        