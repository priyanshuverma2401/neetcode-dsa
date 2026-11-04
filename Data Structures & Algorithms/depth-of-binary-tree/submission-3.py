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
        q = deque()
        q.append(root)
        level = 0

        while q:
            k = len(q)
            for i in range(k):
                front_ele = q.popleft()
                if front_ele.left:
                    q.append(front_ele.left)
                if front_ele.right:
                    q.append(front_ele.right)
            level += 1
        return level
       
             

        