class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if s == " ": return 1

        count_set = set()
        max_length, length = 0, 0
        left, right = 0, 0

        while right < len(s):
            # max_length = max(max_length, len(count_set))
            # max_length = max(max_length, length)
            
            while s[right] in count_set:
                count_set.remove(s[left])
                left+=1
            count_set.add(s[right])
            # length+=1
            max_length = max(max_length, ((right - left) + 1))
            right+=1
        return max_length





        