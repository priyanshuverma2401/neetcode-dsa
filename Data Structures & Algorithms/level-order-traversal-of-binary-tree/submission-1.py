# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if not root: return res
        queue.append(root)

        while queue:
            level_ele = []
            for i in range(len(queue)):
                front_ele = queue.popleft()
                level_ele.append(front_ele.val)
                if front_ele.left:
                    queue.append(front_ele.left)
                if front_ele.right:
                    queue.append(front_ele.right)
            res.append(level_ele)
        return res



        
        