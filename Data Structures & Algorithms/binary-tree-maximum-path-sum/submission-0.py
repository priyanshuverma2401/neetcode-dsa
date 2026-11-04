# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sol(self, root):
        if not root: return 0
        left_path_max = max(0, self.sol(root.left))
        right_path_max = max(0, self.sol(root.right))
        self.res = max(self.res, (root.val + left_path_max + right_path_max))
        return root.val + max(left_path_max, right_path_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        self.sol(root)
        return self.res
        
        
        