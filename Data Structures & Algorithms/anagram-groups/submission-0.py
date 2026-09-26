from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_count = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            freq_count[tuple(count)].append(s)

        print(type(freq_count.values()))
        return list(freq_count.values())