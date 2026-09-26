class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_str1 = [0]*26
        freq_str2 = [0]*26

        for ele in s:
            freq_str1[ord(ele) - ord('a')]+=1
        
        for ele in t:
            freq_str2[ord(ele) - ord('a')] += 1
        
        return freq_str1 == freq_str2
        