class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            character_count = [0 for _ in range(26)]
            for i in range(len(s)):
                character_count[ord(s[i]) - ord('a')] += 1
            
            anagram_dict[tuple(character_count)].append(s)
        
        return list(anagram_dict.values())

        