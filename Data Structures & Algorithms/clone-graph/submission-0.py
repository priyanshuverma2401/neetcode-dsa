"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self, node, oldToNewMap):
        if not node: return node
        if node in oldToNewMap:
            return oldToNewMap[node]

        copy = Node(node.val)
        oldToNewMap[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.clone(nei, oldToNewMap))
        return copy

        

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map_ = {}
        return self.clone(node, map_)
        