class Solution:
    def checkPalindrom(self, left, right, s):
        while left <= right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def doPart(self, index, s, subset):
        if index == len(s):
            self.res.append(subset.copy())
            return
        
        for i in range(index, len(s), 1):
            if self.checkPalindrom(index, i, s):
                subset.append(s[index:i+1])
                self.doPart(i+1, s, subset)
                subset.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.doPart(0, s, [])
        return self.res

        