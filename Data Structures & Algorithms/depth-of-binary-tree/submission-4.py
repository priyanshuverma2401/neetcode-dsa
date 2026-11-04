# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        stack = deque()
        level = 0
        stack.append((root, 1))

        while stack:
            node, lvl = stack.pop()
            level = max(level, lvl)
            if node.right:
                stack.append((node.right, lvl + 1))
            if node.left:
                stack.append((node.left, lvl+1))
            
        return level
        
        