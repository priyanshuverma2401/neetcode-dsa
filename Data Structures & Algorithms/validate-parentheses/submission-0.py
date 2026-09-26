from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        map_p = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }
        queue = []
        for c in s:
            if c == '[' or c == "(" or c == "{":
                queue.append(c)
            else:
                if not queue or map_p[queue[-1]] != c: return False
                queue.pop()
        if not queue: return True
        return False