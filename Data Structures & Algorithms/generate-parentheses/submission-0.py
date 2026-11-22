class Solution:
    def paranthesis(self, count, subset, n):
        if count.get("open", 0) == n and count.get("close", 0) == n:
            substr = "".join(x for x in subset)
            self.res.append(substr)
            return
        
        # decision to put open paranthesis
        if count.get("open", 0) < n:
            subset.append("(")
            count["open"] += 1
            self.paranthesis(count, subset, n)
            subset.pop()
            count["open"]-=1
        
        # decision to put closing paranthesis
        if count.get("open", 0) > count.get("close", 0) and count.get("close", 0) < n:
            subset.append(")")
            count["close"]+=1
            self.paranthesis(count, subset, n)
            count["close"]-=1
            subset.pop()
        
        return



    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        count = {
            "open" : 0,
            "close" : 0
        }

        self.paranthesis(count, [], n)
        return self.res
        