class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = [0 for _ in range(26)]
        left, right = 0, 0
        longest_substring = 0
        while right < len(s):
            length = (right - left) + 1
            freq_count[ord(s[right].lower()) - ord('a')] += 1
            max_freq = max(freq_count)
            if length - max_freq <= k:
                longest_substring = max(longest_substring, (length))
                
            else:
                while left < right and ((right - left) + 1) - max(freq_count) > k:
                    freq_count[ord(s[left].lower()) - ord('a')] -= 1
                    left+=1
            right += 1
        return longest_substring



        