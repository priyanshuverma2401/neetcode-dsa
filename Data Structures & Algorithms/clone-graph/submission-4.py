"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self, root):
        if root in self.oldToNew: return self.oldToNew[root]
        copy = Node(root.val)
        self.oldToNew[root] = copy
        for nei in root.neighbors:
            copy.neighbors.append(self.clone(nei))
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        self.oldToNew = {}
        self.clone(node)
        return self.oldToNew[node]
        