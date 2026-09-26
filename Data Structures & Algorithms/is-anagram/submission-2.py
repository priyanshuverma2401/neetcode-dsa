class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_count = [0]*26
        for c in s:
            character_count[ord(c) - ord('a')]+=1
        
        char_count2 = [0]*26
        for c in t:
            char_count2[ord(c) - ord('a')] += 1
        
        if character_count == char_count2: return True
        return False
        