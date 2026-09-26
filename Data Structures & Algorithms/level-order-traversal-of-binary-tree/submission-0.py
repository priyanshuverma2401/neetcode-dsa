# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        queue.append(root)
        n = len(queue)
        res = []
        if not root: return res
        while queue:
            arr = []
            while n:
                node = queue.popleft()
                arr.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                n-=1
            res.append(arr)
            n = len(queue)
        return res



        
        