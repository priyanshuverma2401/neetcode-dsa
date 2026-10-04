class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count_set = set()
        max_length = 0
        left, right = 0, 0

        while right < len(s):#O(N)
            while s[right] in count_set:
                count_set.remove(s[left])#O(1)
                left+=1
            count_set.add(s[right])#O(N)
            max_length = max(max_length, ((right - left) + 1))
            right+=1
        return max_length

# Space complexity: O(N)
# Time Complexity: O(N)





        