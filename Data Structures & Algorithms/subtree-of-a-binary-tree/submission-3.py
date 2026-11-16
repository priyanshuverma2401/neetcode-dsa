# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False

        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    def checkSubtree(self, root, subtree):
        if not root and not subtree: return True
        if not root: return False
        if not subtree: return True

        if root.val == subtree.val:
            if self.sameTree(root, subtree):
                return True
        
        check_left = self.checkSubtree(root.left, subtree)
        if check_left: return True
        check_right = self.checkSubtree(root.right, subtree)
        if check_right: return True

        return check_left or check_right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.checkSubtree(root, subRoot)

        