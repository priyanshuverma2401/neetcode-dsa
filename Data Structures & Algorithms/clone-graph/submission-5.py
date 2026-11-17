"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneStack(self, root):
        stack = []
        copy = Node(root.val)
        self.oldToNew[root] = copy
        stack.append(root)

        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if self.oldToNew.get(nei, None):
                    self.oldToNew[curr].neighbors.append(self.oldToNew[nei])
                else:
                    copy_nei = Node(nei.val)
                    self.oldToNew[nei] = copy_nei
                    self.oldToNew[curr].neighbors.append(copy_nei)
                    stack.append(nei)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        self.oldToNew = {}
        self.cloneStack(node)
        return self.oldToNew[node]
        