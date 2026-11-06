class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        p_mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif not stack: return False
            else:
                if stack[-1] == p_mapping[s[i]]:
                    stack.pop()
                else: return False
        return True if not stack else False
