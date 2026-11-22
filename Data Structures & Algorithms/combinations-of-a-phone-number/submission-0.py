class Solution:
    def findCombination(self, index, digits, subchar):
        if len(subchar) == len(digits):
            self.res.append(subchar)
            return

        for c in self.charmap[digits[index]]:
            self.findCombination(index+1, digits, subchar + c)
        


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.res = []
        self.charmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        self.findCombination(0, digits, "")
        return self.res
        