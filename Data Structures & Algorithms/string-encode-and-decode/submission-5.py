class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs: #O(N) 
            res += str(len(string)) + "#" + string
        return res
        # Time Complexity: O(N)
        # Space Complexity: O(1)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): #O(len(s))
            j = i
            while s[j] != "#": #O(len(s))
                j+=1
            length = int(s[i : j])
            res.append(s[j+1 : j + length + 1])
            i = j + length + 1
        return res
        # Time Complexity: O(N^2)
        # Space Complexity: O(M) where M is the number of words
