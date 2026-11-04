# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBST(self, minVal, maxVal, node):
        if node.val <= minVal or node.val >= maxVal: return False
        check_left = True
        check_right = True
        if node.left:
            check_left = self.checkBST(minVal, node.val, node.left)
        if node.right:
            check_right = self.checkBST(node.val, maxVal, node.right)
        return check_left and check_right
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(-float('inf'), float('inf'), root)
        