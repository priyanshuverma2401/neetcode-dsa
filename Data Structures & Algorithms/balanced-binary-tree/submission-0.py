# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root):
        if not root: return 0

        left_height = self.check(root.left)
        right_height = self.check(root.right)

        if abs(left_height - right_height) > 1: self.res = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.check(root)
        return self.res
        


        