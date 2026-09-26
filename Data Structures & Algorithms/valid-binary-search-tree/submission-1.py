# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_valid(self, root, minVal, maxVal):
        if not root: return True
        if root.val <= minVal or root.val >= maxVal: return False
        return self.is_valid(root.left, minVal, root.val) and self.is_valid(root.right, root.val, maxVal)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, -float('inf'), float('inf'))
        