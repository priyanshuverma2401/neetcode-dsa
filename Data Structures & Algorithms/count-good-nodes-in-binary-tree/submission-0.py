# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root, prevmax):
        if not root: return 0

        left_good_nodes = self.countNodes(root.left, max(prevmax, root.val))
        right_good_nodes = self.countNodes(root.right, max(prevmax, root.val))
        return (left_good_nodes + right_good_nodes) if root.val < prevmax else (1 + left_good_nodes + right_good_nodes)
        

    def goodNodes(self, root: TreeNode) -> int:
        return self.countNodes(root, root.val)
        

        

        
        