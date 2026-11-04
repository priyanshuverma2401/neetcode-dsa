# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDiameter(self, root):
        if not root: return 0
        left_height = self.findDiameter(root.left)
        right_height = self.findDiameter(root.right)
        self.res = max(self.res, (1 + left_height + right_height))
        return 1 + max(left_height, right_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        self.findDiameter(root)
        return self.res - 1

        