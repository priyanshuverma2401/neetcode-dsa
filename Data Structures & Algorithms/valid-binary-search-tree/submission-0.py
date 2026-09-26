# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, minValue, maxValue):
        if not root: return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        is_left_valid = self.isValid(root.left, minValue, root.val)
        is_right_valid = self.isValid(root.right, root.val, maxValue)

        return is_left_valid and is_right_valid
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -float('inf'), float('inf'))

        