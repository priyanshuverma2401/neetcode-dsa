class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for c in s: #O(N)
            if c == '(' or c == '{' or  c == '[':
                stack.append(c)
            elif stack and c == mapping.get(stack[-1]):
                stack.pop()
            else:
                return False
        return True if not stack else False

# Time complexity: O(N)
# Space Complexity: O(N)

        
        