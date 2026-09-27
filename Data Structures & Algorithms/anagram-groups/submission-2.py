class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs: #O(m) --> m is the total num of ele in strs
            count = [0]*26
            for character in string: #O(n) --> n is the average length of each string
                count[ord(character) - ord('a')] += 1
            res[tuple(count)].append(string)
        # print(list(res.values()))
        return list(res.values())

# Time complexity = O(n.m)
# Space Complexity = O(m.26)